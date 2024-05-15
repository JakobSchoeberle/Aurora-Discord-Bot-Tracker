import os
import asyncio
import discord
import urllib.request
import AuroraToolbox as Toolbox

from urllib.request import urlopen 
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()

@bot.tree.command(name="tonight", description="Forecasted Aurora Viewline for Tonight")
async def slash_command(interaction:discord.Interaction):
    data_url = "https://services.swpc.noaa.gov/experimental/images/aurora_dashboard/tonights_static_viewline_forecast.png"
    pathed_filename = os.path.join("./_media", "tonights_static_viewline_forecast.png")
    urllib.request.urlretrieve(data_url, pathed_filename)
    await interaction.response.send_message(file=discord.File(pathed_filename))

@bot.tree.command(name="tomorrow", description="Forecasted Aurora Viewline for Tomorrow")
async def slash_command(interaction:discord.Interaction):
    data_url = "https://services.swpc.noaa.gov/experimental/images/aurora_dashboard/tomorrow_nights_static_viewline_forecast.png"
    pathed_filename = os.path.join("./_media", "tomorrow_nights_static_viewline_forecast.png")
    urllib.request.urlretrieve(data_url, pathed_filename)
    await interaction.response.send_message(file=discord.File(pathed_filename))

@bot.tree.command(name="now", description="The current Aurora prediction for your moment in time")
async def slash_command(interaction:discord.Interaction):
    embeded=discord.Embed(title="The Aurora Now", description="This is not done yet", color=0xe100ff)
    await interaction.response.send_message(embed=embeded)

@bot.tree.command(name="help", description="Help with using the Aurora Tracker")
async def slash_command(interaction:discord.Interaction):
    embeded=discord.Embed(title="Aurora Borealis Tracker Commands", description="This bot is designed to provide Aurora Borealis Forecast in Discord.\n\n**Commands:**\n•`/tonight` This displays the NOAA Forcast for tonight\n\n•`/tomorrow` This displays the NOAA Forcast for tomorrow\n\n•`/help` You just used this command", color=0xe100ff)
    await interaction.response.send_message(embed=embeded)
'''
@bot.command()
async def ovation(ctx):
    myPath = Toolbox.jsonParser()
    Toolbox.make_gif(myPath)
    pathed_filename = os.path.join("./_media", "Aurora_North.gif")
    await ctx.send(file=discord.File(pathed_filename))
'''
@bot.event # Removed so that it doesn't fuck up the ovation command since that takes so long
async def on_command_error(ctx, error): # Not sure this dones anything anymore
    await ctx.send(str(error))

bot.run(TOKEN)
