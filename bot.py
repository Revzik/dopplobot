import os
import discord
import dotenv

dotenv.load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

    for guild in client.guilds:
        print(f"Connected guilds: [ id: {guild.id}, name: {guild.name} ]")
        print("Members:")
        for member in guild.members:
            print(f" - {member.name}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "ping":
        await message.channel.send("pong")


client.run(TOKEN)
