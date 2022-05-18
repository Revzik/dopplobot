from discord import ClientUser


def connected(user: ClientUser) -> None:
    """
    Handles the action what happens when client connects to Discord.
    Currently, just prints out the message to the console.

    Parameters
    ------------
    user: :class:`~discord.ClientUser`
        bot client object
    """
    print(f"{user} has connected to Discord!")
