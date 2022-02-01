# Import essential discord dependencies
import discord
import requests
from discord.ext import commands
import creategraph as cg


class trade(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='tradehistory', help='Displays stock trade history')
    async def tradehistory(self, ctx, currency1, currency2):
        await ctx.send(f'Returning trade history between {currency1} and {currency2}')
        money_1 = currency1.upper()
        money_2 = currency2.upper()

        r = requests.get(
            f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={money_1}&market={money_2}&apikey={self.bot.alpha_api}&datatype=csv")

        if r.text[0] == '{':
            await ctx.send('Inputs not found: Try using different values or switching the order!')
        else:

            with open('currency.csv', 'w') as f:  # Writes the received csv file to a local file
                f.write(r.text)

            await cg.creategraph(money_1, money_2)  # Creates graph and image (fig1.png)

            with open('fig1.png', 'rb') as f:
                picture = discord.File(f)

            await ctx.send(file=picture)
            await ctx.send('Do you want any more info?')

            def check(m):
                return m.content is not None and m.channel == ctx.channel

            message = await self.bot.wait_for('message', check=check)
            if message.content == 'rate':

                await ctx.send('How many days ago do you want to know the rate of change for?')

                message2 = await self.bot.wait_for('message', check=check)

                try:
                    await ctx.send(f"The rate was {await cg.creategraph(money_1, money_2, -int(message2.content))}")
                except:
                    await ctx.send("Error.")
            else:
                await ctx.send("Wrong input")


def setup(bot):
    bot.add_cog(trade(bot))
