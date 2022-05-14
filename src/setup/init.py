def initial_setup(bot):
    @bot.event
    async def on_ready():
        print(f"{bot.user} has connected to Discord!")


def init_commands(bot):
    from commands import setup_commands
    setup_commands(bot)