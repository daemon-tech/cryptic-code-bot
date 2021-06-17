# bot.py
import os
import dotenv
import discord

from time import sleep
from discord.utils import get
from dotenv import load_dotenv
from discord.ext import commands

from client.reactions import *
from client.listener import *

def cryptic_code_bot_():
    client = discord.Client()
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    
    #reactions_role_checkmark_member()
    def reactions_role_checkmark_member():
        client = discord.Client()
    
    async def on_reaction_add(reaction, user):
        Member = discord.utils.get(user.guild.roles, name="Member")
        if str(reaction.emoji) == "✅":
            await user.add_roles(Member)
            print('Added Role {} to {}'.format(Member, User))
        else:
            print('Booted: on_reaction_add')
            return
    
    listener_()
    
    client.run(TOKEN)
    print('Booted: Bot running.')
    
if __name__ == "__main__" :
    cryptic_code_bot_()