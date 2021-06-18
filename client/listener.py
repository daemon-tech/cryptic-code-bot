from bot import *

def listener_():
    bot = commands.Bot(command_prefix='$')
    client = discord.Client()

    @client.event
    async def on_member_join(member):
        await client.send_message(member,"Welcome!")
        
    print('Booted: listener_')