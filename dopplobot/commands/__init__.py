from discord.ext.commands import Bot, context


def register_commands(bot: Bot) -> None:
    from . import utils

    @bot.command(name="ping")
    async def ping(ctx: context.Context):
        await ctx.send(utils.ping())
