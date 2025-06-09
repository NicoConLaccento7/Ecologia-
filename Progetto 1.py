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

# --- comandi nuovi ---

@bot.command()
async def polistirolo(ctx):
    await ctx.send(f"Il tempo di decomposizione del polistirolo è di circa 1000 anni")

@bot.command()
async def chewinggum(ctx):
    await ctx.send(f"Il tempo di decomposizione della chewing gum è di circa 5 anni")

@bot.command()
async def nylon(ctx):
    await ctx.send(f"Il tempo di decomposizione dei tessuti in nylon è di 30-40 anni")

@bot.command()
async def torsolo(ctx):
    await ctx.send(f"Il tempo di decomposizione del torsolo di mela è di circa 2 settimane")

@bot.command()
async def sigaretta(ctx):
    await ctx.send(f"Il tempo di decomposizione della sigaretta è di 1-2 anni")

@bot.command()
async def banana(ctx):
    await ctx.send(f"Il tempo di decomposizione della banana è di 6 settimane")

@bot.command()
async def Ccotone(ctx):  # <----- La C in maiscolo indica "Capi"
    await ctx.send(f"Il tempo di decomposizione dei capi in cotone varia da 2 a 5 mesi")

@bot.command()
async def gomma(ctx):
    await ctx.send(f"Il tempo di decomposizione della gomma varia da 50 a 80 anni")

# --------------
