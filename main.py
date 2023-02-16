import discord
from discord.ext import commands
import discord.ext.commands
from discord import app_commands
from typing import *
import traceback
import os
import threading

class CustomThread(threading.Thread):
  def __init__(self, command: str):
    threading.Thread.__init__(self)
    self.cmd = command

  def run(self):
    
    os.system(self.cmd)
    
a = CustomThread('node alive.js')
a.start()
    






class Bot(commands.AutoShardedBot):
  def __init__(self):
    intents = discord.Intents.default()
    intents.message_content = True
    
    super().__init__(command_prefix="..", intents=intents, shard_count= 1, help_command= None)
    


  async def on_ready(self):
    servers = len(self.guilds)
    print("\033[0;36;48m-----------------------------------------")
    print(f" * {self.user} connected to {servers} servers")
    
    
    
    print("\033[0;36;48m-----------------------------------------")
    for cmd in self.tree.walk_commands():
      print(cmd.name)
    await self.tree.sync()

    await self.change_presence(activity=discord.Game(name=f"/help | annoying {servers} servers"))
  async def setup_hook(self):
    for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):

        try:
          await bot.load_extension(f'cogs.{filename[:-3]}')
        except Exception:
          print(traceback.format_exc())
        print(f"\033[0;32;49m{filename} loaded")

    
bot = Bot()

bot.run(os.environ['token'])

