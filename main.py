import discord
from discord.ext import commands
import baccarat_logic
import baccarat_simulation
import blackjack_logic
import card
import deck
import roulette_logic
import slots_logic
import slots_simulation

intents = discord.Intents.all()
client = commands.Bot(command_prefix = "r.", self_bot = False, intents=intents)
token = "" #INSERT

@client.event
async def on_connect():
    try:
        print("Connected :)")
    except Exception as e:
        print(f"Err: {e}")

client.run(token, bot=True)