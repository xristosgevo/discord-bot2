import discord
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot ist online als {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "!ping":
        await message.channel.send("Pong!")

client.run(os.getenv("TOKEN"))

