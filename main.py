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
client = commands.Bot(command_prefix = "c.", self_bot = False, intents=intents)
token = "" #INSERT

@client.event
async def on_connect():
    try:
        print("Connected :)")
    except Exception as e:
        print(f"Err: {e}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)

@client.command()
async def test(ctx, param):
    await ctx.reply(param)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.reply("Command not found")
    else:
        await ctx.reply(f"Something went wrong!\n{error}")

client.run(token, bot=True)