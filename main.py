#!/usr/local/bin/python3
import os
from discord.ext import commands
import discord
from dotenv import load_dotenv
import json
import csv
import io
from database import connect
import re

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.messages = True

bot = discord.Client()
@bot.event
async def on_ready():
    print('{bot.user} has connected to Discord!')


bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def champion(ctx, arg):
    champion_items = connect(arg)
    print(champion_items)
    if not champion_items:
        await ctx.send("Champion is not currently in the database")
    else:
        try:
            counter = 1
            for item in champion_items:
                for item_list in item:
                    await ctx.send("Build " + str(counter) + ":")
                    for items in item_list:
                        await ctx.send("\t" + str(items))
                        if item_list.index(items) == len(item_list) - 1:
                            counter += 1
        except:
            await ctx.send("There was an error")
    
bot.run(TOKEN)