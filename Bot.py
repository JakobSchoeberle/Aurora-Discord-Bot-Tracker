import os
import asyncio
import discord
import urllib.request
import AuroraToolbox as Toolbox
import datetime

from urllib.request import urlopen 
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

utc = datetime.timezone.utc

times = [
    datetime.time(hour=8, tzinfo=utc),
    datetime.time(hour=2, minute=5, tzinfo=utc),
    datetime.time(hour=16, minute=40, second=30, tzinfo=utc)
]

#@tasks.loop(time=times)
#async def my_task():
#    await print("My task is running!")

@tasks.loop(seconds=5.0)
async def my_task():
    print("My task is running!")

@bot.event
async def on_ready():
    my_task.start()
    await bot.tree.sync()

@bot.tree.command(name="tonight", description="Forecasted Aurora Viewline for Tonight")
async def slash_command(interaction:discord.Interaction):
    pathed_filename = Toolbox.ImageRetriever("experimental/images/aurora_dashboard/tonights_static_viewline_forecast.png", "./_media")
    await interaction.response.send_message(file=discord.File(pathed_filename))

@bot.tree.command(name="tomorrow", description="Forecasted Aurora Viewline for Tomorrow")
async def slash_command(interaction:discord.Interaction):
    pathed_filename = Toolbox.ImageRetriever("experimental/images/aurora_dashboard/tomorrow_nights_static_viewline_forecast.png", "./_media")
    await interaction.response.send_message(file=discord.File(pathed_filename))

@bot.tree.command(name="latest", description="The current Aurora prediction")
async def slash_command(interaction:discord.Interaction):
    pathed_filename = Toolbox.ImageRetriever("images/animations/ovation/north/latest.jpg", "./_media")
    embeded=discord.Embed(title="The Aurora Now", description="This is not done yet", color=0xe100ff)
    await interaction.response.send_message(file=discord.File(pathed_filename), embed=embeded)

#@bot.tree.command(name="ovation", description="GIF Test")
#async def slash_command(interaction:discord.Interaction):
#    await interaction.response.defer(thinking=True)
#    myPath = Toolbox.jsonParser("./image")
#    Toolbox.make_gif(myPath)
#    pathed_filename = os.path.join("./_media", "Aurora_North.gif")
#    await interaction.followup.send(file=discord.File(pathed_filename))

@bot.tree.command(name="forecast", description="The next 30 to 90 minute Aurora forecast")
async def slash_command(interaction:discord.Interaction):
    await interaction.response.defer(thinking=True)
    pathed_filename = Toolbox.ImageRetriever("experimental/images/aurora_dashboard/tonights_static_viewline_forecast.png", "./_media")
    embeded=discord.Embed(title="The Aurora Now", description="This is not done yet", color=0xe100ff)
    await interaction.followup.send(file=discord.File(pathed_filename), embed=embeded)

@bot.tree.command(name="help", description="Help with using the Aurora Tracker")
async def slash_command(interaction:discord.Interaction):
    embeded=discord.Embed(title="Aurora Borealis Tracker Commands", description="This bot is designed to provide Aurora Borealis Forecast in Discord.\n\n**Commands:**\n•`/tonight` This displays the NOAA Forcast for tonight\n\n•`/tomorrow` This displays the NOAA Forcast for tomorrow\n\n•`/help` You just used this command", color=0xe100ff)
    await interaction.response.send_message(embed=embeded)

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))

bot.run(TOKEN)
