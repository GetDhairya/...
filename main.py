from http import client
import discord
import nextcord
from nextcord.ext import commands
import os

bot = commands.Bot(command_prefix=".", owner_id=896021046585598003)



@bot.event
async def on_ready():
    print(f"{bot.user} is Ready,guilds: {len(bot.guilds)}")
    for file in os.listdir("cogs/"):
        if file.endswith('py'):
            try:
                bot.load_extension(f'cogs.{file[:-3]}')
                print(f"Loaded {file}")
            except Exception as e:
                print(f"Cannot load {file}\n{e}")


@bot.command()
@commands.is_owner()
async def reload(ctx, *, ext):
    try:
        bot.reload_extension(ext)
        await ctx.reply(f"Reloaded {ext}")
    except Exception as e:
        await ctx.reply(f"Cannot reload {ext}\n{e}")


@bot.command(name="servers", aliases=['s', 'server'])
async def _servers(ctx):
    total_servers = len(bot.guilds)
    if total_servers == 0:
        bot.intents = discord.Intents.guilds()
        total_servers = len(bot.guilds)
    embed = discord.Embed(description=f"I am in {total_servers} servers!")
    await ctx.send(embed=embed)

@bot.command()
async def support(self,ctx,*,msg):
    user = await self.client.fetch_user(896021046585598003)
    embed = nextcord.Embed(title=f"Support sent by {ctx.author}")
    embed.description = msg
    await user.send(embed=embed)


bot.run("OTQ3NTIxNTkzMjI2MTk5MDgy.YhuePw.H-9bB4F-POaMLZt6FNtVWf-Q5Tg")
