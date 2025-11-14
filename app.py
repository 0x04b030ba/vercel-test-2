import discord
from discord.ext import commands
from flask import Flask
import os

# Create Flask app to serve a status endpoint
app = Flask(__name__)

# Create a bot instance with the desired prefix "$"
bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

@app.route('/status')
def bot_status():
    if bot.is_ready():
        return "Bot is online!"
    else:
        return "Bot is offline!", 503

# Event: On bot ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

# Ping command (latency)
@bot.command(name='ping')
async def ping(ctx):
    latency = round(bot.latency * 1000)  # Convert latency to ms
    await ctx.send(f'Pong! Latency is {latency}ms')

# Run the Flask app on a separate thread
from threading import Thread
def run_flask():
    app.run(port=5000)

# Start Flask server in the background
Thread(target=run_flask).start()

# Run the bot
bot.run('MTQzODgyNDA0ODExMTkxNTA1OA.G_F6Th.eqlPen_uJ7otISZFLVTs8LhClwBt0xdvEUdbhQ')
