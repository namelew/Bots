import os
import discord
from dotenv import load_dotenv

load_dotenv()
#criar arquivo .env com ambos os dados para acessar as diretivas
token = os.getenv('DISCORD_TOKEN') # tolken de auth
guild = os.getenv('DISCORD_GUILD') # nome do serve

client = discord.Client()

@client.event
async def on_ready():
    for g in client.guilds:
        if g.name == guild:
            break
    print(f'{client.user} has connected to the follow guild:\n{g.name}(id:{g.id})')

    members = '\n - '.join([member.name for member in g.members])
    print(f'Guild Members:\n - {members}')

client.run(token)