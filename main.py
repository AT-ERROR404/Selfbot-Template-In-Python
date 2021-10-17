import asyncio
import discord
from discord.ext import commands

token = "YOUR_TOKEN"
bot = commands.Bot(command_prefix=('YOUR_PREFIX'), self_bot=True)


@bot.event
async def on_message(message):
  await bot.change_presence(activity=discord.Streaming(name="YOUR_STATUS", url="https://www.twitch.tv/github"))
 
@bot.command()
async def example(ctx):
    Your Code
  
bot.run(token, bot=False)
