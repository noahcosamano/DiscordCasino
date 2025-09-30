import discord
from discord.ext import commands
import baccarat_logic.py
import baccarat_simulation.py
import blackjack_logic.py
import card.py
import deck.py
import roulette_logic.py
import slots_logic.py
import slots_simulation.py

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