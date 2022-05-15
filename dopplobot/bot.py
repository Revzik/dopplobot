import os

import dotenv
from discord.ext.commands import Bot

from config import defaults
import setup


if __name__ == "__main__":

    dotenv.load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    if TOKEN is None:
        print("Error: DISCORD_TOKEN cannot be null")
        exit(1)

    bot = Bot(command_prefix=defaults.PREFIX)
    setup.init(bot)

    bot.run(TOKEN)
