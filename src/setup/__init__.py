def register_events(bot):
    from . import events
    @bot.event
    async def on_ready():
        events.connected(bot.user)
