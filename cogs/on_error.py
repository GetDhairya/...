import nextcord
from nextcord.ext import commands
from difflib import get_close_matches


def setup(bot):
    bot.add_cog(Error(bot))


class Error(commands.Cog):
    def __init__(self, bot):

        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, commands.MissingPermissions):
            embed = nextcord.Embed(title="Missing Permission(s)", color=nextcord.Color.red())
            embed.description = f"HAHA,imagine you are trying to use `{ctx.command.name}` without any permission\nYou need `{','.join(error.missing_permissions)}` to use this command,dummy!"
            await ctx.reply(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = nextcord.Embed(title="Missing Required Argument(s)", color=nextcord.Color.red())
            embed.description = f"Hmm,you forgot to give me some argurment(s) for `{ctx.command.name}`,it should be \n ```yaml\n{ctx.clean_prefix}{ctx.command.name} {ctx.command.signature}\n```"
            await ctx.reply(embed=embed)
        elif isinstance(error, commands.CommandNotFound):
            cmds = [i.name for i in self.bot.commands]
            cmd = ctx.invoked_with
            matches = get_close_matches(cmd, cmds)
            if len(matches) == 0:
                embed = nextcord.Embed(title="Command Not Found")
                embed.description = f"Hmmm,I can't find `{cmd}` in my database,maybe you misspelled?"
                await ctx.reply(embed=embed)
            else:
                embed = nextcord.Embed(title="Command Not Found")

                embed.description = f"Hmmm,I can't find `{ctx.clean_prefix}{cmd}`,maybe you meant this?\n ```yaml\n{ctx.clean_prefix}{matches[0]}\n```"
                await ctx.reply(embed=embed)
        else:
            raise error
