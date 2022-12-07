import nextcord
from nextcord.ext import commands
from os import environ
from dotenv import load_dotenv
import auth
import json
import requests

load_dotenv()

token = environ["TOKEN"]

TESTING_GUILD_ID = 872415885321732117  # Replace with your guild ID

#GetBusInfo(url) return response
def GetBusInfo(url):
    a = auth.Auth(auth.app_id, auth.app_key)
    auth_response = auth.requests.post(auth.auth_url, a.get_auth_header())
    d = auth.data(auth.app_id, auth.app_key, auth_response)
    data_response = auth.requests.get(url, headers=d.get_data_header())
    return data_response.json()

RealTimeNearStop_url = 'https://tdx.transportdata.tw/api/basic/v2/Bus/RealTimeNearStop/City/Taichung?%24top=1000&%24format=JSON'
    

def get_json(self, url):
    headers = {'authorization': f'Bearer {self.get_token()}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        j = response.json()
        response.close()
        return j
    else:
        return {
            'error_code': response.status_code,
            'text': response.text
        }

def get_key(dict,value):
    return[k for k, v in dict.items() if v == value]

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')



@bot.slash_command(description="My first slash command", guild_ids=None)
async def bus(interaction: nextcord.Interaction,req_route : str):
    ##dump json to debug##
    #path = 'temp.json'
    #with open(path, 'w') as f:
    #    json.dump(GetBusInfo(RealTimeNearStop_url), f)
    embedVar = nextcord.Embed(title=req_route, description="公車位置", color=0x7FFFD4)
    bus = [[],[]]
    for raw_bus_info in GetBusInfo(RealTimeNearStop_url):
        if raw_bus_info['RouteName']['Zh_tw'] == req_route:
            if raw_bus_info['Direction']:
                bus[0].append(raw_bus_info)
            else:
                bus[1].append(raw_bus_info)
    for bus_info in bus[0]:
        embedVar.add_field(name=bus_info['PlateNumb'], value=bus_info['StopName']['Zh_tw']+str(bus_info['Direction']), inline=False)
    for bus_info in bus[1]:
        embedVar.add_field(name=bus_info['PlateNumb'], value=bus_info['StopName']['Zh_tw']+str(bus_info['Direction']), inline=False)
    await interaction.send(embed=embedVar)


bot.run(token)