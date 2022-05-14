import os
import dotenv

dotenv.load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN is None:
    print("Error: DISCORD_TOKEN cannot be null")
    exit(1)


from discord.ext import commands
from config import defaults
from setup import init


bot = commands.Bot(command_prefix=defaults.PREFIX)
init.initial_setup(bot)
init.init_commands(bot)


bot.run(TOKEN)
