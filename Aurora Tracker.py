import os
import discord
import json
import urllib.request
import AuroraToolbox as Toolbox


from urllib.request import urlopen 
#from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()

@bot.tree.command(name="hello", description="Hello World?")
async def slash_command(interaction:discord.Interaction):
    await interaction.response.send_message("Hello World!")

@bot.tree.command(name="tonight", description="Forecasted Aurora Viewline for Tonight")
async def slash_command(interaction:discord.Interaction):
    data_url = "https://services.swpc.noaa.gov/experimental/images/aurora_dashboard/tonights_static_viewline_forecast.png"
    urllib.request.urlretrieve(data_url, "tonights_static_viewline_forecast.png")
    await interaction.response.send_message(file=discord.File('tonights_static_viewline_forecast.png'))

@bot.tree.command(name="tomorrow", description="Forecasted Aurora Viewline for Tomorrow")
async def slash_command(interaction:discord.Interaction):
    data_url = "https://services.swpc.noaa.gov/experimental/images/aurora_dashboard/tomorrow_nights_static_viewline_forecast.png"
    urllib.request.urlretrieve(data_url, "tomorrow_nights_static_viewline_forecast.png")
    await interaction.response.send_message(file=discord.File('tomorrow_nights_static_viewline_forecast.png'))

@bot.tree.command(name="help", description="Help with using the Aurora Tracker")
async def slash_command(interaction:discord.Interaction):
    embeded=discord.Embed(title="Aurora Borealis Tracker Commands", description="This bot is designed to provide Aurora Borealis Forecast in Discord.\n\n**Commands:**\n•`/tonight` This displays the NOAA Forcast for tonight\n\n•`/tomorrow` This displays the NOAA Forcast for tomorrow\n\n•`/help` You just used this command", color=0xe100ff)
    await interaction.response.send_message(embed=embeded)

@bot.tree.command(name="Dev", description="Testing Command")
async def slash_command(interaction:discord.Interaction):
    embeded=discord.Embed(title="Aurora Borealis Tracker Commands", description="This bot is designed to provide Aurora Borealis Forecast in Discord.\n\n**Commands:**\n•`/tonight` This displays the NOAA Forcast for tonight\n\n•`/tomorrow` This displays the NOAA Forcast for tomorrow\n\n•`/help` You just used this command", color=0xe100ff)
    await interaction.response.send_message(embed=embeded)

@bot.event
async def on_command_error(ctx, error):
    await ctx.send("An error has occurred")

'''

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

'''

bot.run(TOKEN)