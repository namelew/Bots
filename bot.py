import os
import discord
from dotenv import load_dotenv

load_dotenv()
#criar arquivo .env com ambos os dados para acessar as diretivas
token = os.getenv('DISCORD_TOKEN') # tolken de auth
guild = os.getenv('DISCORD_GUILD') # nome do serve

class CustomClient(discord.Client):
    async def on_ready(self):
        g = discord.utils.get(self.guilds, name=guild)
        print(f'{self.user} has connected to the follow guild:\n{g.name}(id:{g.id})')

        members = '\n - '.join([member.name for member in g.members])
        print(f'Guild Members:\n - {members}')

client = CustomClient()
client.run(token)