import os
import discord
from discord import embeds
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
#criar arquivo .env com ambos os dados para acessar as diretivas
token = os.getenv('DISCORD_TOKEN') # tolken de auth
guild = os.getenv('DISCORD_GUILD') # nome do serve

bot = commands.Bot("!")

@bot.event
async def on_ready():
    print(f"{bot.user} conectado ao Discord!")

@bot.command(name="oi")
async def oi(ctx):
    name = ctx.author.name
    await ctx.send(f"Olá, {name}")
bot.run(token)