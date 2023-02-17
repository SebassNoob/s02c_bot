import discord
from discord.ext import commands
from discord import app_commands
from typing import *
import re

class Helper(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

    
  
  @app_commands.command(name = "customrole", description = "Give yourself a custom role!")
  @app_commands.describe(colour="The hex code of your role colour", name = "The name of your custom role")
  async def color(self, interaction: discord.Interaction, colour: app_commands.Range[str, 6, 6], name: str):
    
    #validate
    if not re.search("^([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$", colour):
      
      await interaction.response.send_message("❌ Enter a valid hex code, idiot.", ephemeral=True)
      return

    role = await interaction.guild.create_role(name=name, color = int(colour, 16))
    await interaction.user.add_roles(role)
    await interaction.response.send_message(f"created role {name} with hex code {colour}")

  @app_commands.command(name = 'help', description = 'displays a help menu')
  async def help(self, interaction: discord.Interaction):
    res = discord.Embed(color=0x000000).set_author(name='s02c help')
    res.add_field(name = "/customrole (color) (name)", value = "give yourself a custom colour role!")
    await interaction.response.send_message(embed = res)

async def setup(bot):
  await bot.add_cog(Helper(bot))