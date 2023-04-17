
from discord.ext import commands
import discord
BOT_TOKEN = #Insert Discord BOT Private Token String Here
CHANNEL_ID = #Insert Discord Channel ID String for bot access
            
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
@bot.event

async def on_ready():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("DiscordBot is online!")
    
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")
    
@bot.command()
async def add(ctx, *arr):
    result = 0
    index = 0
    for i in arr:
        index = float(i)
        result += index
    await ctx.send(f"Result: {result}")
    
@bot.command()
async def multiply(ctx, *arr):
    result = 1
    index = 0
    for i in arr:
        index = float(i)
        result = result*index
    await ctx.send(f"Result: {result}")
    
    
    
bot.run(BOT_TOKEN)
