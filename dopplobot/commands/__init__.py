def register_commands(bot):
    from . import utils

    @bot.command(name="ping")
    async def ping(ctx):
        await ctx.send(utils.ping())
