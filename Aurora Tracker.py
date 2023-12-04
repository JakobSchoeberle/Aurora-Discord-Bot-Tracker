import os
import discord
import json
import urllib.request
import glob

from urllib.request import urlopen 
from discord.ext import commands
from dotenv import load_dotenv
from PIL import Image

def make_gif(frame_folder):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.jpg")]
    frame_one = frames[0]
    frame_one.save("Aurora_North.gif", format="GIF", append_images=frames,
               save_all=True, duration=100, loop=0)

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
    lenght=len(data)
    #await ctx.send(lenght)
    for index in range(210, lenght):
        x = json.dumps(data[index])
        #await ctx.send(data[0])
        y = json.loads(x)
        data_url = "https://services.swpc.noaa.gov/" + y["url"]
        image_name = "aurora_North_" + str(index) + ".jpg"
        myPath = ".\image"
        fullfilename = os.path.join(myPath, image_name)
        #await ctx.send(fullfilename)
        urllib.request.urlretrieve(data_url, fullfilename)
    make_gif(myPath)
    await ctx.send(file=discord.File('Aurora_North.gif'))

@bot.command()
async def tonight(ctx):
    data_url = "https://services.swpc.noaa.gov/experimental/images/aurora_dashboard/tonights_static_viewline_forecast.png"
    urllib.request.urlretrieve(data_url, "tonights_static_viewline_forecast.png")
    await ctx.send(file=discord.File('tonights_static_viewline_forecast.png'))

@bot.command()
async def tomorrow(ctx):
    data_url = "https://services.swpc.noaa.gov/experimental/images/aurora_dashboard/tomorrow_nights_static_viewline_forecast.png"
    urllib.request.urlretrieve(data_url, "tomorrow_nights_static_viewline_forecast.png")
    await ctx.send(file=discord.File('tomorrow_nights_static_viewline_forecast.png'))

@bot.command()
async def info(ctx):
    embed=discord.Embed(title="Aurora Borealis Tracker Commands", description="This bot is designed to provide Aurora Borealis Forecast in Discord.\n\n**Commands:**\n•`$tonight` This displays the NOAA Forcast for tonight\n\n•`$tomorrow` This displays the NOAA Forcast for tomorrow\n\n•`$help` Shows the commands kinda like this\n\n•`$info` Shows this thing", color=0xe100ff)
    await ctx.send(embed=embed)

#@bot.event
#async def on_command_error(ctx, error):
#    await ctx.send("That's not a command")

bot.run(TOKEN)