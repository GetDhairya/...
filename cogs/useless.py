import nextcord
from nextcord.ext import commands

def setup(bot):
  bot.add_cog(Useless(bot))
class Useless(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
