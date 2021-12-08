from importlib.util import decode_source
import os
import datetime
from typing import Text
from aiohttp.http import RESPONSES
from discord import emoji
import requests
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


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "Oi" in message.content:
        await message.channel.send(f"Olá, {message.author.name}. Bem vindo ao servidor")

    await bot.process_commands(message)

@bot.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == "👍":
        role = user.guild.get_role(918156867836985364)
        await user.add_roles(role)
    elif reaction.emoji == "😆":
        role = user.guild.get_role(918157003984109629)
        await user.add_roles(role)

@bot.command() # default é o nome da função
async def binance(ctx, coin, base):
    try:
        response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")
        data = response.json()
        price = data.get("price")
        if price:
            await ctx.send(f"O valor do {coin}/{base} é {price}")
        else:
            await ctx.send(f"O par {coin}/{base} é inválido")
    except Exception as error:
        await ctx.send("Ops... Ocorreu um erro")
        print(error)

@bot.command("segredo")
async def secret(ctx):
    try:
        await ctx.author.send("Só você receberá essa mensagem")
    except discord.errors.Forbidden:
        await ctx.send("Não pude te contar o segredo, habilite receber mensagem de todos do servidor")

@bot.command("foto")
async def get_random_imag(ctx):
    url_image = "https://picsum.photos/200/300"

    embed = discord.Embed(
        title="Resultado da busca de imagem",
        description="Essa imagem é totalmente aleatória",
        color=0x0000FF
    )

    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.set_footer(text=f"Feito por {bot.user.name}", icon_url=bot.user.avatar_url)
    embed.add_field(name="API", value="Usamos a api da " + url_image)
    embed.add_field(name="Parâmetros", value="{largura}/{altura}")
    embed.add_field(name="Exemplo", value=url_image, inline=False)
    embed.set_image(url=url_image)

    await ctx.send(embed=embed)


bot.run(token)