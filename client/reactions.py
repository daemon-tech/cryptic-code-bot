import discord

from client.bot import *

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