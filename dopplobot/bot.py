import os
import dotenv

dotenv.load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN is None:
    print("Error: DISCORD_TOKEN cannot be null")
    exit(1)


from discord.ext.commands import Bot
from config import defaults
from setup import register_events
from commands import register_commands


bot = Bot(command_prefix=defaults.PREFIX)
register_events(bot)
register_commands(bot)


bot.run(TOKEN)
