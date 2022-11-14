import nextcord
from nextcord.ext import commands
from os import environ
from dotenv import load_dotenv
import auth
import json

load_dotenv()

token = environ["TOKEN"]

TESTING_GUILD_ID = 872415885321732117  # Replace with your guild ID

#GetBusInfo(url) return response
def GetBusInfo(url):
    a = auth.Auth(auth.app_id, auth.app_key)
    auth_response = auth.requests.post(auth.auth_url, a.get_auth_header())
    d = auth.data(auth.app_id, auth.app_key, auth_response)
    data_response = auth.requests.get(url, headers=d.get_data_header())
    return data_response.text
path = 'temp.json'
with open(path, 'w') as f:
    json.dump(GetBusInfo('https://tdx.transportdata.tw/api/basic/v2/Bus/RealTimeByFrequency/City/Taichung?%24top=30&%24format=JSON'), f)

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description="My first slash command", guild_ids=[TESTING_GUILD_ID])
async def bus(interaction: nextcord.Interaction):
    await interaction.send()


bot.run(token)