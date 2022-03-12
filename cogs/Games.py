import nextcord
from nextcord.ext import commands
import random
import asyncio
import random
import copy



def get_embed(_title, _description, _color):
    return nextcord.Embed(title=_title, description=_description, color=_color)


class games(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fi(self, ctx):
        """
        Impostors can sabotage the reactor,
        which gives Crewmates 30–45 seconds to resolve the sabotage.
        If it is not resolved in the allotted time, The Impostor(s) will win.
        """

        embed1 = nextcord.Embed(title="Who's the imposter?",
                                description="Find out who the imposter is, before the reactor breaks down!",
                                color=0xff0000)

        embed1.add_field(name='Red', value='<:red:942272322218373150>', inline=False)
        embed1.add_field(name='Blue', value='<:blue:942272321970909244>', inline=False)
        embed1.add_field(name='Lime', value='<:lime:942272323287937044>', inline=False)
        embed1.add_field(name='White', value='<:white:942272322474229801>', inline=False)

        msg = await ctx.send(embed=embed1)

        # imposter : emoji
        emojis = {
            'red': '<:red:942272322218373150>',
            'blue': '<:blue:942272321970909244>',
            'lime': '<:lime:942272323287937044>',
            'white': '<:white:942272322474229801>'
        }

        # pick the imposter
        imposter = random.choice(list(emojis.items()))
        imposter = imposter[0]

        # add all possible reactions
        for emoji in emojis.values():
            await msg.add_reaction(emoji)

        # check whether the correct user responded.
        # also check its a valid reaction.
        def check(reaction, user):
            self.reacted = reaction.emoji
            return user == ctx.author and str(reaction.emoji) in emojis.values()

        # waiting for the reaction to proceed
        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=30.0, check=check)

        except asyncio.TimeoutError:
            # defeat, reactor meltdown
            description = "Reactor Meltdown.{0} was the imposter...".format(imposter)
            embed = get_embed("Defeat", description, nextcord.Color.red())
            await ctx.send(embed=embed)
        else:
            # victory, correct answer
            if str(self.reacted) == emojis[imposter]:
                description = "**{0}** was the imposter...".format(imposter)
                embed = get_embed("Victory", description, nextcord.Color.blue())
                await ctx.send(embed=embed)

            # defeat, wrong answer
            else:
                for key, value in emojis.items():
                    if value == str(self.reacted):
                        description = "**{0}** was not the imposter...".format(key)
                        embed = get_embed("Defeat", description, nextcord.Color.red())
                        await ctx.send(embed=embed)
                        break

def setup(client):
    client.add_cog(games(client))

