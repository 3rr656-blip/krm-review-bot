import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")

# Put your reviews channel ID here

CHANNEL_ID = 123456789012345678

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

```
if message.channel.id == CHANNEL_ID:
    await message.channel.send(GIF_URL)

await bot.process_commands(message)
```

bot.run(TOKEN)
