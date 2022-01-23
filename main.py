# Import essential discord dependencies
import discord
from discord.ext import commands

# Discord Setup
intents = discord.Intents.default()
intents.members = True
apiToken = f"{DiscordApiToken}"

# Bot Setup
bot = commands.Bot(command_prefix='.', intents=intents)
cogs = ['Trade']
bot.auth_users = [907839431640223774, 166262833745625088, 278478019394404353]


# Bot Body

@bot.event
async def on_ready():  # When our project successfully connects to Discord
    print('The bot is connected')
    debug_channel = await bot.fetch_channel(934259234743390250)
    await debug_channel.send("Bot is running @everyone")


if __name__ == "__main__":  # Loading other files
    for cog in cogs:
        bot.load_extension(cog)

bot.run(apiToken)
