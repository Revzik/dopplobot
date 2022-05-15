from discord.ext.commands import Bot


def register_events(bot: Bot) -> None:
    """
    Sets up all the other events handled by the bot.

    Parameters
    ------------
        bot :class:`~discord.ext.commands.Bot`: bot object that will register the events
    """
    from . import events

    @bot.event
    async def on_ready():
        events.connected(bot.user)


def init(bot: Bot) -> None:
    """
    Initializes the ``bot`` object. Takes care of registering events and commands to which the bot can respond

    Parameters
    ------------
        bot :class:`~discord.ext.commands.Bot`: bot object to setup
    """
    import commands

    register_events(bot)
    commands.register_commands(bot)
