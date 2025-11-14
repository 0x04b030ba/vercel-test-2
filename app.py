import discord
from discord.ext import commands
import os
from flask import Flask

# Initialize Flask app
app = Flask(__name__)

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

# Create a simple route for Flask to check the bot status
@app.route('/status')
def bot_status():
    return "Bot is running!"

# Run the Flask app to expose an endpoint for status check
if __name__ == "__main__":
    app.run(debug=True)
    bot.run('MTQzODgyNDA0ODExMTkxNTA1OA.G_F6Th.eqlPen_uJ7otISZFLVTs8LhClwBt0xdvEUdbhQ')
