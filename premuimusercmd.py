from http import client
import json
import discord
import nextcord
from nextcord.ext import commands
import os
from discord.ext.commands import check
bot = commands.Bot(command_prefix=".", owner_id=896021046585598003)



def check_if_user_has_premium(ctx):
    with open("premium.json") as f:
        premium_users_list = json.load(f)
        if ctx.author.id not in premium_users_list:
            return False

    return True
@bot.command()
@check(check_if_user_has_premium)
async def apremiumcommand(ctx):
    await ctx.send("Hello premium user!")

@apremiumcommand.error
async def apremiumcommand_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
            await ctx.send("Sorry, but you are not a premium user!")
    else:
        raise error