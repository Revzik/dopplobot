from discord import ClientUser


def connected(user: ClientUser) -> None:
    """
    Handles the action what happen when client connects to Discord

    Parameters
    ------------
        user :class:`~discord.ClientUser`: bot client object
    """
    print(f"{user} has connected to Discord!")
