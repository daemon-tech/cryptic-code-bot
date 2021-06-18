import os
from time import sleep

def pip_os_(module):
    if os.name == 'nt':
        pip_os_ = 'pip install {}'.format(module)
        return pip_os_
    else:
        pip_os_ == 'python3 -m pip install {}'.format(module)
        return pip_os_

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
        
def boot():
    if os.name == 'nt':
        os.system('py3 /client/bot.py')
    else:
        os.system('python3 client/bot.py')

try:
    import dotenv
    import discord
    from time import sleep
    from dotenv import load_dotenv
    from discord.utils import get  
except ModuleNotFoundError:
    print('Modules incorrectly installed!')
    print('Modules: Auto installing...')
    sleep(2)
    pip_os_("python-dotenv")
    pip_os_("-U discord.py")
    clear()
    print('Modules: Importing Now')
    try:
        import dotenv
        import discord
        from time import sleep
        from dotenv import load_dotenv
        from discord.utils import get  
    except ModuleNotFoundError:
        print("Modules incorrectly installed!")
        sleep(3)
        close()
    
print('Modules: All Modules found.')
print('Booting the Bot...')
sleep(2)
boot()