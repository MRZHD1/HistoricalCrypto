# Import essential discord dependencies
import discord
from discord.ext import commands

# Discord Setup
intents = discord.Intents.default()
intents.members = True
discord_api = input("Input your discord bot API token here: \n")
alpha_api = input("Input your alpha vantage api key here: \n")

# Bot Setup
bot = commands.Bot(command_prefix='.', intents=intents)
bot.alpha_api = alpha_api
cogs = ['trade']


# Bot Body

@bot.event
async def on_ready():  # When our project successfully connects to Discord
    print('The bot is connected')


if __name__ == "__main__":  # Loading other files
    for cog in cogs:
        bot.load_extension(cog)

bot.run(discord_api)
