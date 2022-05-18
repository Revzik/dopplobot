from discord.ext.commands import Bot, context


def register_commands(bot: Bot) -> None:
    """
    Sets up all the static commands handled by the bot.

    Parameters
    ------------
    bot: :class:`~discord.ext.commands.Bot`
        bot object that will register the commands
    """
    from . import utils

    @bot.command(name="ping")
    async def ping(ctx: context.Context):
        await ctx.send(utils.ping())
