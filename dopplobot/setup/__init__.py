def register_events(bot):
    from . import events

    @bot.event
    async def on_ready():
        events.connected(bot.user)


def init(bot):
    import commands

    register_events(bot)
    commands.register_commands(bot)
