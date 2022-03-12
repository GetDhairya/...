import nextcord
from nextcord.ext import commands


def setup(bot):
    bot.add_cog(RR(bot))


class ReactionButtons(nextcord.ui.View):
    def __init__(self):
        self.timeout = 0


def check_if_emoji(ctx, string: str):
    try:
        emoji = commands.EmojiConverter().convert(ctx, string)
        return emoji
    except:
        return None


def check_emoji(ctx, _list):
    checked = 0
    for i in _list:
        if check_if_emoji(ctx, i) == None:
            pass
        else:
            checked += 1
        if checked == len(_list):
            return True
        else:
            return False


class RR(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def reactionrole(self, ctx, *, text):
        all = text.split(',')
        global emoji
        emoji = [i[0] for i in [i.split(';') for i in all]]
        if check_emoji(ctx, emoji):
            print(emoji)
            id = [i[1] for i in [i.split(';') for i in all]]
            role_id = [int(i) for i in id]
            print(role_id)
            roles = []
            for i in role_id:
                role = ctx.guild.get_role(i)
                roles.append(role)

            messages = []
            for i in range(len(emoji)):
                messages.append(f"{emoji[i]}: {roles[i].mention}")
            msgs = '\n'.join(messages)
            emb = nextcord.Embed(title="Reaction Role!")
            emb.description = msgs
            await ctx.send(embed=emb)

    # what help u need?
