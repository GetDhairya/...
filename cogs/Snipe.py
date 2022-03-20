import asyncio
import time
import nextcord
from nextcord.ext import commands

class Snipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

snipe_message_content = None
snipe_message_author = None
snipe_content_author = None
content = None
@commands.Cog.listener()
async def on_message_delete(message):
    snipe_content_author.remove(None)
    content.remove(None)
    content.append(message.content) 
    snipe_content_author.append(message.author.id) 
    await asyncio.sleep(60)
    snipe_content_author.remove(message.author.id)
    content.remove(message.content)
    
    

@commands.command()
async def snipe(self,ctx):
    if snipe_message_content==None:
        await ctx.send("Theres nothing to snipe.")
    else:
        embed = nextcord.Embed(description=f"{content}")
        embed.set_footer(text=f"Asked by {ctx.author.name} #{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        embed.set_author(name= f"<@{snipe_content_author}>")
        await ctx.send(embed=embed)
        return

def setup(bot):
    bot.add_cog(Snipe(bot))