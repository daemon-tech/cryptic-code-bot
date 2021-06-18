import discord

from bot import *
from on_ready import *

def reactions_role_add_member():
    client = discord.Client()
    bot = discord.Client(intents=discord.Intents.all())
    
    print('Debug: Waiting on Action')
    
    @client.event
    async def on_raw_reaction_add(data, user):
        
        print('Debug: Waiting IF data.member.user.bot')
        
        if data.member.user.bot:
            print('Debug: RETURN')
            return
        if data.channel.id == 854826582639640626:
            if data.message_id == 854833029348720640:
                if data.emoji == '✅':
                    print('Debug: DATA.EMOJI FOUND -> MEMBER =')
                    Member = discord.utils.get(user.guil.roles, name='Member')
                    print('Debug: AWAIT USER.ADD...')
                    await user.add_roles(Member)
    print('Booted: reactions_role_add_member()')
                    