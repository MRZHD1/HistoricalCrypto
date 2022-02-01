# HistoricalCrypto 

HistoricalCrypto is a bot that allows easy access to historical trading information on a public social media platform. It utilizes the AlphaVantage API to pull cryptocurrency trading information from the site and converts that information into an elegant graph. It also contains the functionality to calculate the instantaneous rate of change at any recent date using a custom-built derivative calculator. 

# Setup 

Firstly, you need to run the setup.py to install all the required files. After that, you need two API keys: 

* A discord bot’s API key. You can find how to set this up and invite your bot [here.][1] 

* An AlphaVantage API key. You can get one [here.][2]

 

# Usage 

There is one command using HistoricalCrpyto, `.tradehistory`, which takes in two arguments; the cryptocurrency you’re wishing to graph, and the fiat currency you’re wishing to contrast it with. After that, the bot asks if you need any more information, after which you may input the only acceptable argument, `‘rate’`. It then asks for input on how many days ago you need it for, which accepts positive integer values up to `800`. 

 

# Example 
![alt text](https://cdn.discordapp.com/attachments/907846889179844629/937884034967691304/unknown.png)

[1]: https://discordpy.readthedocs.io/en/stable/discord.html
[2]: https://www.alphavantage.co/support/
