import discord

from bot import *

def on_ready_():
    client = discord.Client()
    bot = discord.Client(intents=discord.Intents.all())
    
    @bot.event
    async def on_ready():
        print('BotID: {} - Name: {}'.format(bot.user.id, bot.user.name))

    print('Booted: on_ready')