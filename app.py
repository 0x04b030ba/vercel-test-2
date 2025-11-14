import discord
from discord.ext import commands

# Create a bot instance with the desired prefix "$"
bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

# Event: On bot ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

# Ping command (latency)
@bot.command(name='ping')
async def ping(ctx):
    latency = round(bot.latency * 1000)  # Convert latency to ms
    await ctx.send(f'Pong! Latency is {latency}ms')

# Run the bot with your token
bot.run('MTQzODgyNDA0ODExMTkxNTA1OA.G_F6Th.eqlPen_uJ7otISZFLVTs8LhClwBt0xdvEUdbhQ')
