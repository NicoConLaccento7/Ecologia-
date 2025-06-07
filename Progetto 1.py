import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f"Hai fatto l\'accesso come {bot.user}")


@bot.command()
async def plastica(ctx):
    await ctx.send(f"Il tempo di decomposizione della plastica è circa 1000 anni")

@bot.command()
async def carta(ctx):
    await ctx.send(f"Il tempo di decomposizione della carta varia da 6 a 12 settimane")

@bot.command()
async def cartone(ctx):
    await ctx.send(f"Il tempo di decomposizione del cartone varia da 2 a 5 anni, in base allo spessore")

@bot.command()
async def alluminio(ctx):
    await ctx.send(f"Il tempo di decomposizione dell' alluminio può arrivare anche a 100 anni")
    
@bot.command()
async def vetro(ctx):
    await ctx.send(f"Il tempo di decomposizione del vetro è circa 4000 anni")

@bot.command()
async def legno(ctx):
    await ctx.send(f"Il tempo di decomposizione del legno varia da 1 a 3 anni")

bot.run("MTM2ODEzMTkzNjQ5MjcxNjEzMw.GAAV4v.T7oRaUaYPFdfzW9Ngau6o9S_vOZOrXVsXGKGxg")
