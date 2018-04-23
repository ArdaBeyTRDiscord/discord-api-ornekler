import discord
from discord import Game
import asyncio
client = discord.Client()

@client.event
async def on_ready():
    print('Bot Giriş yaptı, Bilgileri:')
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(game=Game(name="istediginiz oyun"))
client.run('sanırımtoken')
