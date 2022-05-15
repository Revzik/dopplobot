from discord.ext.commands import Bot


def register_events(bot: Bot) -> None:
    from . import events

    @bot.event
    async def on_ready():
        events.connected(bot.user)


def init(bot: Bot) -> None:
    import commands

    register_events(bot)
    commands.register_commands(bot)
