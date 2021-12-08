import os
import datetime
import discord
from discord import channel
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
#criar arquivo .env com ambos os dados para acessar as diretivas
token = os.getenv('DISCORD_TOKEN') # tolken de auth
guild = os.getenv('DISCORD_GUILD') # nome do serve

bot = commands.Bot("!")

@bot.event
async def on_ready():
    print(f"{bot.user} conectado ao Discord!")
    current_time.start()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "Oi" in message.content:
        await message.channel.send(f"Olá, {message.author.name}. Bem vindo ao servidor")

    await bot.process_commands(message)

@bot.command(name="oi")
async def oi(ctx):
    name = ctx.author.name
    await ctx.send(f"Olá, {name}")

@tasks.loop(seconds=10)
async def current_time():
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%y às %H:%M:%S")
    channel = bot.get_channel(917795118365433910)
    await channel.send(f"Data atual: {now}")

bot.run(token)