def ping_command(bot):
    @bot.command(name="ping")
    async def ping(ctx):
        await ctx.send("pong")
