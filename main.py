import discord
import requests
import json

from misc import *
from keys import *
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix = '-', intents=intents)

@client.event
async def on_ready():
    print("Successfully Initialized\n--------------------------")
    
@client.command()
async def hello(ctx):
    await ctx.send("Hey! My name's Kaspar, but you can call me Kas ;3")
    
@client.command()
async def goodbye(ctx):
    await ctx.send("Goodbye c:")
    
@client.event
async def on_member_join(member):
    url = "https://dad-jokes.p.rapidapi.com/random/joke"

    headers = {
        "X-RapidAPI-Key": JOKE,
        "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    #print(json.loads(response.text)['body'][0]['setup'])
   
    print('Detected User Join')

    channel = client.get_channel(1119286047759671397)
    await channel.send("User Join Detected")
    laugh = choose_laugh()
    await channel.send(json.loads(response.text)['body'][0]['setup'] + '\n' + json.loads(response.text)['body'][0]['punchline'] + choose_laugh())
    
@client.event
async def on_member_remove(member):
    channel = client.get_channel(1119286047759671397)
    #await channel.send("User Leaving Detected")
    print('Detected User Leaving')
    
client.run(TOKEN)