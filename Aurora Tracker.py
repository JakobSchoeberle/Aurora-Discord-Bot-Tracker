import os
import discord
import json
import urllib.request
from urllib.request import urlopen 
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def ovation(ctx):
    url = "https://services.swpc.noaa.gov/products/animations/ovation_north_24h.json"
    json_url = urlopen(url)
    data = json.loads(json_url.read())
    x = json.dumps(data[1])
    y = json.loads(x)
    data_url = "https://services.swpc.noaa.gov/" + y["url"]
    urllib.request.urlretrieve(data_url, "aurora_N.jpg")
    await ctx.send(file=discord.File('aurora_N.jpg'))

@bot.command()
async def tomorrow(ctx):
    data_url = "https://services.swpc.noaa.gov/experimental/images/aurora_dashboard/tomorrow_nights_static_viewline_forecast.png"
    urllib.request.urlretrieve(data_url, "tomorrow_nights_static_viewline_forecast.png")
    await ctx.send(file=discord.File('tomorrow_nights_static_viewline_forecast.png'))

@bot.command()
async def tonight(ctx):
    data_url = "https://services.swpc.noaa.gov/experimental/images/aurora_dashboard/tonights_static_viewline_forecast.png"
    urllib.request.urlretrieve(data_url, "tonights_static_viewline_forecast.png")
    await ctx.send(file=discord.File('tonights_static_viewline_forecast.png'))

@bot.command()
async def info(ctx):
    embed=discord.Embed(title="Aurora Borealis Tracker Commands", description="This bot is designed to provide Aurora Borealis Forecast in Discord.\n\n**Commands:**\n•`$tonight` This displays the NOAA Forcast for tonight\n\n•`$tomorrow` This displays the NOAA Forcast for tomorrow\n\n•`$help` Shows the commands kinda like this\n\n•`$info` Shows this thing", color=0xe100ff)
    await ctx.send(embed=embed)

bot.run(TOKEN)