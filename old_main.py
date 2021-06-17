import os
from time import sleep
from client.reactions import reactions_role_checkmark_member
from client.bot import *

gitrepo = 'https://github.com/le3ch-tech/dc-role-assign-bot.git'

def dicord_py_module():
    if os.name == 'nt':
        dicord_py_module = 'pip install discord.py'
        return dicord_py_module
    else:
        dicord_py_module = 'python3 -m pip install discord.py'
        return dicord_py_module
    
def dotenv_module():
    if os.name == 'nt':
        dotenv_module = 'pip install python-dotenv'
        return dicord_py_module
    else:
        dotenv_module = 'python3 -m pip install python-dotenv'
        return dotenv_module

def clear():
    if os.name == 'nt':
        clear_ = 'clr'
        return clear_
    else:
        clear_ = 'clear'
        return clear_
        
def clone_git_():
    system.os('git clone https://github.com/le3ch-tech/dc-role-assign-bot.git')

try:
    try:
        import discord.py
        import dotenv
        from client.bot import *
    except ModuleNotFoundError:
        print('Modules incorrectly installed!')
        sleep(1)
        if ModuleNotFoundError() == discord.py:
            print('Module: Discord.py not installed')
            print('Would you like to install it?')
            dcpy_ = input('Y / N')
            if dcpy_ == 'y' | dcpy_ == 'Y':
                print('Installing...')
                sleep(1)
                system.os(dicord_py_module())
            else:
                print('Closing in 3 seconds')
                sleep(3)
                exit()
    
        elif ModuleNotFoundError() == dotenv:
            print('Module: dotenv_module not installed')
            print('Would you like to install it?')
            dcpy_ = input('Y / N')
            if dcpy_ == 'y' | dcpy_ == 'Y':
                print('Installing...')
                sleep(1)
                system.os(dotenv_module())
            else:
                print('Closing in 3 seconds')
                sleep(3)
                exit()

        else:
            print('Client isnt installed. Please reinstall')
            print('git clone: {}'.format(gitrepo))
            sleep(1)
            clone_git_ = input('Clone Git Repo?')  
            if clone_git_ == 'y' | clone_git_ == 'Y':
                clone_git_()
            else:
                print('Closing in 3 seconds')
                sleep(3)
                exit()
except:
    print('Unknown Error: Pass')
    sleep(2)
    os.system(clear())
    pass
            
cryptic_code_bot_()