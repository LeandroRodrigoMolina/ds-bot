import discord
from discord.ext import commands
import random
import token_1
import requests
import aiohttp
with open("curiosidadJapones.txt", "r", encoding="utf-8") as file:
    curiosidades_japones = file.readlines()

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()
async def duda(ctx):
    i = random.randint(0, len(curiosidades_japones) - 1)
    # Crear un embed
    color_hex = "2E0B36"
    color_int = int(color_hex, 16)
    embed = discord.Embed(
        title="Curiosidad sobre el Japonés",  # Título del embed
        description=curiosidades_japones[i],   # Descripción (tu curiosidad)
        color=color_int  # Color del borde del embed
    )
    embed.set_image(url="https://yt3.googleusercontent.com/8-ce7p9udKhfyTpEtsNzvVLEZB4GfjVXz93IHzhZ0NtN0ozM3IvtlzSpHH0F150u_SFFqxqTuw=s176-c-k-c0x00ffffff-no-rj")
    await ctx.send(embed=embed)

@client.command()
async def h(ctx):
    #url = 'https://api.lolicon.app/setu/v2'
    url = 'https://api.lolicon.app/setu/v2?tag=%E8%90%9D%E8%8E%89&r18=0&size=small'

    async with aiohttp.ClientSession() as session:

        async with session.get(url) as response:

            if response.status == 200:
                data = await response.json()
                imagen = data["data"][0]["urls"]["small"]
                color_int = 16711680
                embed = discord.Embed(
                    title="Andas hot?",  # Título del embed
                    description="Mensaje hot",   # Descripción
                    color=color_int  # Color del borde del embed
                )
                embed.set_image(url=imagen)
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Error en la petición: {response.status}")

client.run(token_1.token())