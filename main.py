import os 
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Cargar el token del archivo .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Intents (permite recibir ciertos eventos de Discord)
intents = discord.Intents.default()
intents.message_content = True

# Prefijo de comandos, por ejemplo: !hola
bot = commands.Bot(command_prefix="!", intents=intents)

# Evento: cuando el bot se conecta
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

# Comando: !hola
@bot.command()
async def hola(ctx):
    await ctx.send(f"¡Hola {ctx.author.name}! Soy tu bot.")


@bot.command()
async def anunciar(ctx):
    canal = bot.get_channel(1378106007422767117)
    if canal:
        await canal.send("¡Este es un anuncio en un canal específico!")
    else:
        await ctx.send("No pude encontrar ese canal.")


# Iniciar el bot
bot.run(TOKEN)
