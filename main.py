from http import client
import json
import discord
import nextcord
from nextcord.ext import commands
import os
from discord.ext.commands import check
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
    '''Only owner of bot which is me XXXX#0007'''
    try:
        bot.reload_extension(ext)
        await ctx.reply(f"Reloaded {ext}")
    except Exception as e:
        await ctx.reply(f"Cannot reload {ext}\n{e}")


@bot.command(name="servers", aliases=['s', 'server'])
async def _servers(ctx):
    '''tells in how many server it is in'''
    total_servers = len(bot.guilds)
    if total_servers == 0:
        bot.intents = discord.Intents.guilds()
        total_servers = len(bot.guilds)
    embed = discord.Embed(description=f"I am in {total_servers} servers!")
    await ctx.send(embed=embed)


@bot.command()
async def info(ctx):
    '''Basic Bot Info.'''
    embed = discord.Embed(title="Community bot", description="It is a bot for games ,moderation and ecomnomy system comming soon", color=000000) #,color=Hex code
    embed.add_field(name="Creator", value="XXXX#0007")
    embed.add_field(name="Invite", value="https://discord.com/api/oauth2/authorize?client_id=947521593226199082&permissions=8&scope=bot")
    embed.set_image(url="https://www.bing.com/th?id=OIP.620tdFe3agmiXG4KJE-dcAHaFj&w=288&h=216&c=8&rs=1&qlt=90&o=6&dpr=1.25&pid=3.1&rm=2")
    embed.set_thumbnail(url="https://www.bing.com/th?id=OIP.620tdFe3agmiXG4KJE-dcAHaFj&w=288&h=216&c=8&rs=1&qlt=90&o=6&dpr=1.25&pid=3.1&rm=2")
    await ctx.send(embed=embed)

@bot.command()
async def invite(ctx):
    '''Invite bot to ur server'''
    embed = discord.Embed(title="Community bot", description="It is a bot for games ,moderation and ecomnomy system comming soon", color=000000) #,color=Hex code
    embed.add_field(name="Creator", value="XXXX#0007")
    embed.add_field(name="Invite", value="https://discord.com/api/oauth2/authorize?client_id=947521593226199082&permissions=8&scope=bot")
    embed.set_image(url="https://www.bing.com/th?id=OIP.620tdFe3agmiXG4KJE-dcAHaFj&w=288&h=216&c=8&rs=1&qlt=90&o=6&dpr=1.25&pid=3.1&rm=2")
    embed.set_thumbnail(url="https://www.bing.com/th?id=OIP.620tdFe3agmiXG4KJE-dcAHaFj&w=288&h=216&c=8&rs=1&qlt=90&o=6&dpr=1.25&pid=3.1&rm=2")
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def say(ctx,message):
    '''Says a msg only one word'''
    if(len(message)==0):
        em = discord.Embed()
        em.title = f'Usage: /say [x]'
        em.description = f'Says whatever is after /say'
        em.add_field(name="Example", value="/say hello\n\n>hello", inline=False)
        em.color = 0x22BBFF
        await ctx.send(embed=em)
        return
    phrase = ""
    for word in message:
        phrase += word
    await ctx.send(phrase)

@bot.command(pass_context=True)
async def ping(ctx,help=""):
    '''Latency * 1000'''
    if(help.find('help')!=-1):
        em = discord.Embed()
        em.title = f'Usage: /ping'
        em.description = f'Prints the bot latency from the host server to Discord servers'
        em.add_field(name="Example", value="/ping", inline=False)
        em.color = 0x22BBFF
        await ctx.send(embed=em)
        return
    import platform
    em = discord.Embed()
    em.title = f'Ping - \n   Latency:'
    em.description = f'{bot.ws.latency * 1000:.4f} ms'
    em.color = 0xFFA400
    await ctx.send(embed=em)

@bot.command(pass_context=True)
async def test(ctx,help="",amount="10"):
    '''test say check complete'''
    await ctx.send(str("Check completed "))
    print(ctx.author.id)
    
@bot.command(pass_context=True)
async def spam(ctx,help="",amount="10"):   
    '''spam 1 to 10 only once'''
    for x in range (11):
        await ctx.send(str(x))

@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('Hey there! This server looks good but need moderation bot and is now here....:)) . \nI have many games and other utilites alsp')
        break

@bot.command(pass_context=True)
async def support(ctx):
    embed = discord.Embed(title="Support", description="discord id - XXXX#0007 \n support server comming soon", color=0x0072ff)
    embed.set_footer(text="Support is here")
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def ui(ctx, user: discord.Member):
    '''Info of a user the join date has a bug'''
    embed = discord.Embed(title="{}'s Info".format(user.name), description="Here's What I could Find in Discord's Database!", color=0x0072ff)
    embed.add_field(name="Name", value=user.name)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Role", value=user.top_role, inline=True)
    embed.add_field(name="Joined At", value=user.joined_at, inline=True)
    embed.set_footer(text="Userinfo")
    await ctx.send(embed=embed)


@bot.command(pass_content=True)
async def poll(ctx, *, text: str):
    poll = await ctx.send(f"{text}")
    await poll.add_reaction("✅")
    await poll.add_reaction("❌")


bot.help_command = None
@bot.command(pass_context=True,aliases=['commands','commandlist','command','h'])
async def help(ctx):
    em = discord.Embed()
    em.title = '_**Commands**_'
    em.color = 0x22BBFF
    em.description = f"For more information on a command, run .help cmd'\n"
    em.add_field(name="\u200b", value="__**General Commands**__", inline=False)
    em.add_field(name=".ping", value="Gets latency from bot host to Discord servers", inline=True)
    em.add_field(name=".nitro", value="Rickroll friends", inline=True)
    em.add_field(name=".help", value="Gets this cmd", inline=True)
    em.add_field(name=".say", value="Makes bot say what you put in PHRASE", inline=True)
    em.add_field(name=".s", value="finds servers it is in", inline=True)
    em.add_field(name=".info / .invite", value="Both does same thing", inline=True)
    em.add_field(name=".poll", value="Ask poll  ", inline=True)
    em.add_field(name="\u200b", value="*_*Games**", inline=False)
    em.add_field(name=".howgay", value=".howgay @user", inline=True)
    em.add_field(name=".fi", value="Amongus game", inline=True)
    em.add_field(name=".snake", value="Sanke game", inline=True)

    em.add_field(name="\u200b", value="__**Other**__", inline=False)
    em.add_field(name=".test", value="test the bot says check complete", inline=True)
    em.add_field(name=".spam", value="Make bot spam from 1 to 10", inline=True)
    em.add_field(name=".ui", value="finds detail abt someone else . The time is wrng", inline=True)
    em.add_field(name=".snipe", value="Finds deleted msg", inline=True)
    #em.add_field(name="/python CODE", value="```diff\n-Runs CODE as Python code, only works for specific users due to some security and execution concerns```", inline=True)

    await ctx.send(embed=em)
    ## Message cuts off soon due to max embed size capacity, start a new embed
    em = discord.Embed()
    em.title = '_**Moderation commands**_'
    em.color = 0x22BBFF
    em.add_field(name=".ban", value="Bans a user. cmd - .ban @user", inline=True)
    em.add_field(name=".kick", value="Kicks a user. cmd - .kick @user", inline=True)
    em.add_field(name=".mute", value="timeouts a user. cmd - .mute @user", inline=True)
    em.add_field(name=".unban", value="UNBans a user. cmd - .unban user id", inline=True)
    em.add_field(name=".tempban", value="tempBans a user. cmd - .tempban @user time", inline=True)


    await ctx.send(embed=em)




bot.sniped_messages = {}
  
@bot.event
async def on_message_delete(message):
  bot.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)
    
@bot.command()
async def snipe(ctx):
  try:
    contents, author, channel_name, time = bot.sniped_messages[ctx.guild.id]
        
  except:
    await ctx.channel.send("I can't find a message to snip.")
    return
  embed = discord.Embed(description=contents,
                        color=ctx.author.color,
                        timestamp=time)
  embed.set_author(name=f"{author.name}#{author.discriminator}",)
  embed.set_footer(text=f"Deleted in #{channel_name}")
    
  await ctx.send(embed=embed)

bot.run("OTQ3NTIxNTkzMjI2MTk5MDgy.YhuePw.iR8DYb4ipWbCmJarLT8JHZtePeI")
