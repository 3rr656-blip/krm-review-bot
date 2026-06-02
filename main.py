import os
import threading
from flask import Flask
import discord
from discord.ext import commands

# Web server for Render
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is online!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

threading.Thread(target=run_web).start()

# Discord Bot
TOKEN = os.getenv("TOKEN")

CHANNEL_ID = 123456789012345678  # Replace with your channel ID

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

GIF_URL = "https://cdn.imageurlgenerator.com/uploads/eb4776a7-0b0b-4ef6-9f8c-564365313af4.gif"

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id == CHANNEL_ID:
        await message.channel.send(GIF_URL)

    await bot.process_commands(message)

bot.run(TOKEN)
