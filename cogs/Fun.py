import nextcord
from nextcord.ext import commands

class nitro(commands.Cog):
    def init(self, bot):
        self.bot = bot

    @commands.command()
    async def nitro(self, ctx):
      embed = nextcord.Embed(title="You've been gifted a subscription!", description="You've been gifted nitro for 1 year!")
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/841319732454883369/938687737433841674/image0.jpg")
      view = Green()
      await ctx.send(embed=embed, view=view)

class Green(nextcord.ui.View):
    def __init__(self):
     super().__init__()
     self.value = None

    @nextcord.ui.button(label="Accept", style=nextcord.ButtonStyle.green)
    async def kekw(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
      await interaction.response.send_message("https://tenor.com/view/rick-roll-gif-23595798", ephemeral=True)
      self.value = True

def setup(bot):
    bot.add_cog(nitro(bot))