import nextcord
from nextcord.ext import commands
from os import environ
from dotenv import load_dotenv
import auth

load_dotenv()

token = environ["TOKEN"]

TESTING_GUILD_ID = 872415885321732117  # Replace with your guild ID

a = auth.Auth(auth.app_id, auth.app_key)
auth_response = auth.requests.post(auth.auth_url, a.get_auth_header())
d = auth.data(auth.app_id, auth.app_key, auth_response)
data_response = auth.requests.get(auth.url, headers=d.get_data_header())

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description="My first slash command", guild_ids=[TESTING_GUILD_ID])
async def bus(interaction: nextcord.Interaction):
    await interaction.send(data_response.text)


bot.run(token)