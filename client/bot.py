# bot.py
import os
import dotenv
import discord

from time import sleep
from discord.utils import get
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get

from reactions import *
from on_ready import *
from listener import *
from clear_ import *

clear_()

client = discord.Client()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_message(message):
    if message.channel.id == 854826582639640626:
        if message.content.startswith('roles'):
            embedvar = discord.Embed(title="React to this Emoji!",
                                     description="Click the corresponding emoji to accept the rules.\n<:yes:855447870466555914> - Member", color=0x00ff00)
            await message.channel.send(embed=embedvar)
            print("Changed message embed color.")
        elif message.content.startswith('update'):
            embedvar2 = discord.Embed(title="React to this Emoji!",
                                      description="Click the corresponding emoji to accept the rules. \n<:yes:855447870466555914> - Member", color=0x00ff00)
            
            channel = client.get_channel(854826582639640626)
            msg = await channel.fetch_message(855471027592888331)
            await msg.edit(embed=embedvar2)
            print("Updated: Embed Role Message")
            await message.channel.send("Updated: Embed Role Message")
    else:
        return
    
@client.event
async def on_raw_reaction_add(payload):
    # channel and message IDs should be integer:
    if payload.channel_id == 854826582639640626 and payload.message_id == 855471027592888331:
        if str(payload.emoji) == "<:yes:855447870466555914>":
            guild = client.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            role = get(payload.member.guild.roles, name='Member')
            await payload.member.add_roles(role)
            print(f"Assigned {member} {role}.")
    
print("Server Running")

print('Booted: Successfully Booted')
client.run(TOKEN)
    