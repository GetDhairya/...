import nextcord
from nextcord.ext import commands
import random
import asyncio
import copy


def setup(bot):
    bot.add_cog(Game(bot))


global get_embed


def get_embed(_title, _description, _color):
    return nextcord.Embed(title=_title, description=_description, color=_color)


class SnakeGame:
    def __init__(self, board):
        self.length = 1
        self.snake = [[len(board) // 2, len(board[0]) // 2]]
        self.direction = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
        self.board = board
        self.make_apple()

    def has_won_snake(self):
        return self.length == 100

    def get_head_position(self):
        return self.snake[0]

    def point(self, pt):
        if self.length > 1 and (pt[0] * -1, pt[1] * -1) == self.direction:
            pass
        else:
            self.direction = pt

    def move(self):
        cur = self.snake[0]
        x, y = self.direction
        new = [cur[0] + x, cur[1] + y]
        if len(self.snake) > 2 and new in self.snake[2:]:
            return True
        if new[0] >= len(self.board):
            new[0] = 0
        elif new[0] == -1:
            new[0] = len(self.board) - 1
        if new[1] >= len(self.board[0]):
            new[1] = 0
        elif new[1] == -1:
            new[1] = len(self.board[0]) - 1
        if tuple(new) == self.apple:
            self.board[self.apple[0]][self.apple[1]] = ' '
            self.make_apple()
            self.length += 1
        self.snake.insert(0, new)
        if len(self.snake) > self.length:
            self.snake.pop()

    def get_board(self):
        board = copy.deepcopy(self.board)
        for row in self.snake:
            board[row[0]][row[1]] = 's'
        return board

    def make_apple(self):
        x = random.randint(0, len(self.board) - 1)
        y = random.randint(0, len(self.board[0]) - 1)
        while [x, y] in self.snake:
            x = random.randint(0, len(self.board) - 1)
            y = random.randint(0, len(self.board[0]) - 1)
        self.board[x][y] = 'a'
        self.apple = x, y


class Buttons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    global check_win

    def check_win(_input, dank):
        win = {
            "paper": "rock",
            "scissors": "paper",
            "rock": "scissors"
        }
        lose = {
            "paper": "scissors",
            "scissors": "rock",
            "rock": "paper"
        }

        if win[_input] == dank:
            return "win"
        elif lose[_input] == dank:
            return "lose"
        elif _input == dank:
            return "tie"

    global emojis
    emojis = {
        "paper": "<:Paper:951091035814109215>",
        "rock": "<:Rock:951090826006642689>",
        "scissors": "<:zb_scissor:951090370014511105>"
    }

    @nextcord.ui.button(emoji="<:Rock:951090826006642689>")
    async def rock(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        user = random.choice(["rock", "paper", "scissors"])
        if check_win("rock", user) == "lose":
            embed = nextcord.Embed(title="Rock Paper Scissors!")
            embed.description = f"**Dank Memer**:\n{emojis[user]}\n\n**Player(You)**:\n{emojis['rock']}\n\n**Dank Memer Won!**"
            embed.set_author(name="Dank Memer",
                             icon_url="https://cdn.discordapp.com/avatars/270904126974590976/d60c6bd5971f06776ba96497117f7f58.png?size=64")
            b1 = self.children
            for item in b1:
                item.disabled = True
            await msg.edit(embed=embed, view=self)
        elif check_win("rock", user) == "win":
            embed = nextcord.Embed(title="Rock Paper Scissors!")
            embed.description = f"**Dank Memer**:\n{emojis[user]}\n\n**Player(You)**:\n{emojis['rock']}\n\n**You Won!**"
            embed.set_author(name="Dank Memer",
                             icon_url="https://cdn.discordapp.com/avatars/270904126974590976/d60c6bd5971f06776ba96497117f7f58.png?size=64")
            b1 = self.children
            for item in b1:
                item.disabled = True
            await msg.edit(embed=embed, view=self)
        elif check_win("rock", user) == "tie":
            embed = nextcord.Embed(title="Rock Paper Scissors!")
            embed.description = f"**Dank Memer**:\n{emojis[user]}\n\n**Player(You)**:\n{emojis['rock']}\n\n**Tie.**"
            embed.set_author(name="Dank Memer",
                             icon_url="https://cdn.discordapp.com/avatars/270904126974590976/d60c6bd5971f06776ba96497117f7f58.png?size=64")
            b1 = self.children
            for item in b1:
                item.disabled = True
            await msg.edit(embed=embed, view=self)

    @nextcord.ui.button(emoji="<:Paper:951091035814109215>")
    async def paper(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        user = random.choice(["rock", "paper", "scissors"])
        if check_win("paper", user) == "lose":
            embed = nextcord.Embed(title="Rock Paper Scissors!")
            embed.description = f"**Dank Memer**:\n{emojis[user]}\n\n**Player(You)**:\n{emojis['paper']}\n\n**Dank Memer Won!**"
            embed.set_author(name="Dank Memer",
                             icon_url="https://cdn.discordapp.com/avatars/270904126974590976/d60c6bd5971f06776ba96497117f7f58.png?size=64")
            b1 = self.children
            for item in b1:
                item.disabled = True
            await msg.edit(embed=embed, view=self)
        elif check_win("paper", user) == "win":
            embed = nextcord.Embed(title="Rock Paper Scissors!")
            embed.description = f"**Dank Memer**:\n{emojis[user]}\n\n**Player(You)**:\n{emojis['paper']}\n\n**You Won!**"
            embed.set_author(name="Dank Memer",
                             icon_url="https://cdn.discordapp.com/avatars/270904126974590976/d60c6bd5971f06776ba96497117f7f58.png?size=64")
            b1 = self.children
            for item in b1:
                item.disabled = True
            await msg.edit(embed=embed, view=self)
        elif check_win("paper", user) == "tie":
            embed = nextcord.Embed(title="Rock Paper Scissors!")
            embed.description = f"**Dank Memer**:\n{emojis[user]}\n\n**Player(You)**:\n{emojis['paper']}\n\n**Tie.**"
            embed.set_author(name="Dank Memer",
                             icon_url="https://cdn.discordapp.com/avatars/270904126974590976/d60c6bd5971f06776ba96497117f7f58.png?size=64")
            b1 = self.children
            for item in b1:
                item.disabled = True
            await msg.edit(embed=embed, view=self)

    @nextcord.ui.button(emoji="<:zb_scissor:951090370014511105>")
    async def scissors(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        user = random.choice(["rock", "paper", "scissors"])
        if check_win("scissors", user) == "lose":
            embed = nextcord.Embed(title="Rock Paper Scissors!")
            embed.description = f"**Dank Memer**:\n{emojis[user]}\n\n**Player(You)**:\n{emojis['scissors']}\n\n**Dank Memer Won!**"
            embed.set_author(name="Dank Memer",
                             icon_url="https://cdn.discordapp.com/avatars/270904126974590976/d60c6bd5971f06776ba96497117f7f58.png?size=64")
            b1 = self.children
            for item in b1:
                item.disabled = True
            await msg.edit(embed=embed, view=self)
        elif check_win("rock", user) == "win":
            embed = nextcord.Embed(title="Rock Paper Scissors!")
            embed.description = f"**Dank Memer**:\n{emojis[user]}\n\n**Player(You)**:\n{emojis['scissors']}\n\n**You Won!**"
            embed.set_author(name="Dank Memer",
                             icon_url="https://cdn.discordapp.com/avatars/270904126974590976/d60c6bd5971f06776ba96497117f7f58.png?size=64")
            b1 = self.children
            for item in b1:
                item.disabled = True
            await msg.edit(embed=embed, view=self)
        elif check_win("scissors", user) == "tie":
            embed = nextcord.Embed(title="Rock Paper Scissors!")
            embed.description = f"**Dank Memer**:\n{emojis[user]}\n\n**Player(You)**:\n{emojis['scissors']}\n\n**Tie.**"
            embed.set_author(name="Dank Memer",
                             icon_url="https://cdn.discordapp.com/avatars/270904126974590976/d60c6bd5971f06776ba96497117f7f58.png?size=64")
            b1 = self.children
            for item in b1:
                item.disabled = True
            await msg.edit(embed=embed, view=self)


class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.client = bot

    @commands.command()
    async def howgay(self, ctx, *, user: commands.MemberConverter):
        user_val = random.randint(0, 100)
        ctx_val = random.randint(0, 100)
        embed = nextcord.Embed(title="Howgay")
        embed.add_field(name=f"{ctx.author.name}", value=f"{ctx_val}%")
        embed.add_field(name=user.name, value=f"{user_val}%")

        if user_val > ctx_val:
            embed.description = f"{user.mention} Won!"
        elif user_val < ctx_val:
            embed.description = f"{ctx.author.mention} Won!"
        await ctx.send(embed=embed)

    def format_board(self, board, snake_head):
        lst = []
        dct = {'a': '🍑', 'S': '😄', 's': '🟢', ' ': '⬛'}
        for x, row in enumerate(board):
            scn_lst = []
            for y, column in enumerate(row):
                if [x, y] == snake_head:
                    scn_lst.append(dct["S"])
                else:
                    scn_lst.append(dct[column])
            lst.append(''.join(scn_lst))
        return '\n'.join(lst)

    @commands.command()
    async def snake(self, ctx):
        board = [[' ' for _ in range(10)] for _ in range(10)]
        UP = (-1, 0)
        DOWN = (1, 0)
        LEFT = (0, -1)
        RIGHT = (0, 1)
        conversion = {'⬅': LEFT, '⬆': UP, '➡': RIGHT, '⬇': DOWN}
        s = SnakeGame(board)
        embed = nextcord.Embed(title='Snake', description=self.format_board(s.get_board(), s.get_head_position()),
                               color=nextcord.Color.blurple())
        msg = await ctx.send(embed=embed)
        emojis = ['⬅', '⬆', '➡', '⬇']
        for emoji in emojis:
            await msg.add_reaction(emoji)
        while True:
            await msg.edit(
                embed=nextcord.Embed(title='Snake', description=self.format_board(s.get_board(), s.get_head_position()),
                                     color=nextcord.Color.blurple()))
            try:
                reaction, _ = await self.client.wait_for('reaction_add', check=lambda r, u: u == ctx.author and str(
                    r) in emojis and r.message == msg, timeout=1.5)
            except asyncio.TimeoutError:
                lost = s.move()
            else:
                try:
                    await msg.remove_reaction(str(reaction), ctx.author)
                except nextcord.Forbidden:
                    pass

                s.point(conversion[str(reaction)])
                lost = s.move()
            if lost:
                await ctx.send('Your snake bit itself :pensive:')
                break
            if s.has_won_snake():
                await ctx.send('you won!!!')
                break

    @commands.command()
    async def rockpaperscissor(self, ctx):
        embed = nextcord.Embed(title="Rock Paper Scissors!")
        embed.description = "**Dank Memer**:\nChoosing <a:Loading:951086998951702528>\n\n**Player(You)**:\nChoosing <a:Loading:951086998951702528>"
        embed.set_author(name="Dank Memer",
                         icon_url="https://cdn.discordapp.com/avatars/270904126974590976/d60c6bd5971f06776ba96497117f7f58.png?size=64")
        global msg
        msg = await ctx.send(embed=embed, view=Buttons())

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
            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)

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
