import asyncio
import random

import nextcord
from nextcord.ext import commands


class Giveaway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gstart(self, ctx, time=None,*, prize=None):
        if time is None:
            return await ctx.send('pls mention the time')
        if prize is None:
            return await ctx.send(f'wass the prize{ctx.author.mention}')
        await ctx.send(':tada: **GIVEAWAY TIME** :tada:')
        embed = nextcord.Embed(title=f"**{prize}**", description=f"React with 🎉 to participate\nEnds in {time}",
                               color=0x2ecc71)
        embed.add_field(name='Hosted by:', value=f'{ctx.author.mention} thank him in the chat :tada:')
        time_convert = {"s": 1, 'm': 60, 'h': 3600, 'd': 86400}
        gawtime = int(time[0]) * time_convert[time[-1]]
        embed.set_footer(text=f'Giveaway Ends in {time}')
        gaw_msg = await ctx.send(embed=embed)

        await gaw_msg.add_reaction("🎉")
        await asyncio.sleep(gawtime)

        new_gaw_msg = await ctx.channel.fetch_message(gaw_msg.id)

        users = await new_gaw_msg.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))

        winner = random.choice(users)

        guild = ctx.guild

        winning_announcement = nextcord.Embed(color=0xff2424)
        winning_announcement.set_author(name=f'THE GIVEAWAY HAS ENDED!', icon_url='https://i.imgur.com/DDric14.png')
        winning_announcement.add_field(name=f'🎉 Prize: {prize}',
                                       value=f'🥳 **Winner**: {winner.mention}\n 🎫 **Number of Entrants**: {len(users)}',
                                       inline=False)
        winning_announcement.set_footer(text='Thanks for entering!')
        winning_announcement2 = nextcord.Embed(color=0xff2424)
        winning_announcement2.add_field(name=f'Y-You won the gaw of {prize} in the server of {guild}', value='🎉')
        winning_announcement2.add_field(name=f'🎉 Prize: {prize}',
                                        value=f'🥳 **Winner**: {winner.mention}\n 🎫 **Number of Entrants**: {len(users)}',
                                        inline=False)
        winning_announcement2.set_footer(text='Thanks for entering!')
        await ctx.send(embed=winning_announcement)
        await winner.send(embed=winning_announcement2)


def setup(bot):
    bot.add_cog(Giveaway(bot))