import nextcord
from nextcord.ext import commands
from os import environ
from dotenv import load_dotenv

load_dotenv()

token = environ["TOKEN"]

TESTING_GUILD_ID = 872415885321732117  # Replace with your guild ID

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description="My first slash command", guild_ids=[TESTING_GUILD_ID])
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Hello!")

bot.run(token)