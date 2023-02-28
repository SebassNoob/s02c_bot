import discord
from discord.ext import commands
from discord import app_commands
from typing import *
import re
import random
import asyncio


class Shit(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

    
  @app_commands.command(name="textwall", description="Sends a wall of repeated text in a single message")
  @app_commands.describe(num = "The number of times to spam", content="What to spam")
  async def textwall(self, interaction: discord.Interaction, num:int, content: str, tts: Optional[bool] = False):
    
    toSend = ' '.join([content.strip() for i in range(num)])
    
    if len(toSend) > 2000:
      await interaction.response.send_message("❌ Your text wall is too long (>2000 characters), you moron.")
      return
    
    await interaction.response.send_message(toSend, tts = tts)

  @app_commands.command(name = "ghosttroll", description = "Ghostpings a user in 3 different channels")
  @app_commands.describe(user="The user to ping")
  @app_commands.guild_only()
  async def ghosttroll(self, interaction: discord.Interaction ,user: discord.Member):
    


    allowedChannels = []
    
    for channel in interaction.guild.channels:
      if channel.permissions_for(user).send_messages and str(channel.type) ==  'text':
        
        allowedChannels.append(channel.id)

    if len(allowedChannels) != 0:
      await interaction.response.send_message("The user will be ghost pinged in 3 channels to annoy them.")   
    else: 
      await interaction.response.send_message("That user can't access any channels, bruh wtf")  

    i = 3
    while i !=0:
      
      try:
        targetChannel = self.bot.get_channel(random.choice(allowedChannels))
        
          
        message = await targetChannel.send("{}".format(user.mention))
        await asyncio.sleep(0.1)
        await message.delete()
        i-=1
        await asyncio.sleep(1)
        

      except Exception:
        continue

  @app_commands.command(name = "nitrotroll", description = "Sends a fake nitro embed")
  async def nitrotroll(self, interaction: discord.Interaction):
    em = discord.Embed(color = 0x7289da, title = "A wild gift appears!", description = "Nitro classic (3 months)\nThis link will expire in 12 hours, claim it now!").set_thumbnail(url ="https://i.imgur.com/w9aiD6F.png")
    
    class claim(discord.ui.View):
      def __init__(self):
        super().__init__()

      @discord.ui.button(label="Claim", style=discord.ButtonStyle.green)
      async def claim(self, interaction: discord.Interaction, button: discord.ui.Button):
        button.style = discord.ButtonStyle.grey
        button.disabled = True
        em = discord.Embed(color = 0x000000, title = "You received a gift, but...", description = "The gift link has either expired or has been revoked.\nThe sender can still create a new link to send again.").set_thumbnail(url ="https://i.imgur.com/w9aiD6F.png")
        await interaction.response.edit_message(embed = em, view=self)
        await interaction.followup.send(content="You idiot lol\nhttps://c.tenor.com/x8v1oNUOmg4AAAAd/rickroll-roll.gif", ephemeral=True)
        
    await interaction.response.send_message(content=".")
    msg = await interaction.original_response()
    await msg.delete()
    await interaction.channel.send(content = "https://dicsord.com/gifts/84329801239480219834", embed = em, view = claim())



async def setup(bot):
  await bot.add_cog(Shit(bot))