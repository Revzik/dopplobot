from discord import ClientUser


def connected(user: ClientUser) -> None:
    print(f"{user} has connected to Discord!")
