import datetime
from http import client
import nextcord
from nextcord import user
from nextcord.ext import commands
import humanfriendly
import asyncio
import time
import humanfriendly
import discord

def setup(bot):
    bot.add_cog(Moderation(bot))


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # kick commands

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: nextcord.Member, reason: str = "No reason provied."):
        '''kicks member syntax .kick @user reson'''
        if ctx.author.top_role.position > user.top_role.position:
            await ctx.guild.kick(user, reason=f"Kicked by {ctx.author.name},Reason: {reason}")
            await ctx.send(f"Kicked **{user.name}** with reason *{reason}*")
            embed = nextcord.Embed(title="You are KICKED",
                                   description=f"You were KICKED in   {ctx.guild.name} with the reason: **{reason}** \n Who did this? *{ctx.author.name}*")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/947738056662876240/947805134233174026/tumblr_d90582c52660338d67dd8687dc8c3aaa_9f3ab55d_1280.gif")
            await user.send(embed=embed)
        else:
            await ctx.send("Bruh,imagine you want to kick a guy that is higher than you")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: nextcord.Member, reason: str = "No reason provied."):
        '''ban member syntax .ban @user reson'''
        if ctx.author.top_role.position >= user.top_role.position:
            await ctx.guild.ban(user, reason=f"Banned by {ctx.author.name},Reason: {reason}")
            await ctx.send(f"Banned **{user.name}** with reason *{reason}*")
            embed = nextcord.Embed(title="You are BANNED",
                                   description=f"You were BANNED in   {ctx.guild.name} with the reason: **{reason}** \n Who did this? *{ctx.author.name}*")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/947738056662876240/947805134233174026/tumblr_d90582c52660338d67dd8687dc8c3aaa_9f3ab55d_1280.gif")
            await user.send(embed=embed)
        else:
            await ctx.send("Bruh,imagine you want to kick a guy that is higher than you")

    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def unban(self , ctx, member: nextcord.User):
        '''unban member syntax .unban userid'''
        guild = ctx.guild
        embed = nextcord.Embed(title=f"✅  {member} has successfully unbaned", color=0x2ECC71)
        if ctx.author.guild_permissions.ban_members:
            await ctx.send(embed=embed)
            await guild.unban(user=member)
        else:
            await ctx.send("Bruh,imagine you want to unban is guy that is higher than you")

    @commands.command(pass_context=True)
    @commands.has_permissions(moderate_members=True)
    async def mute(self, ctx,  user: nextcord.Member, time, *, reason=None):
        '''mute member syntax .mute @user time reson'''
        time = humanfriendly.parse_timespan(time)
        await user.edit(timeout=nextcord.utils.utcnow() + datetime.timedelta(seconds=time))
        await asyncio.sleep(2)
        await ctx.send(f"**{user.name}** has been timeout because {reason}.")


  