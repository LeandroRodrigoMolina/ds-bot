import discord
from discord.ext import commands
from discord import *
import random
import token_1
import aiohttp
import asyncio

from AudioButton import AudioButton

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()
async def curiosidad(ctx):
    # Leer el archivo para determinar el número de curiosidades
    print(ctx.author.id)
    with open("curiosidadJapones.txt", "r", encoding="utf-8") as file:
        curiosidades_japones = file.readlines()
    i = random.randint(0, len(curiosidades_japones) - 1)
    # Crear un embed
    color_hex = "2E0B36"
    color_int = int(color_hex, 16)
    embed = discord.Embed(
        title="Curiosidad sobre el Japonés",  # Título del embed
        description=curiosidades_japones[i],  # Descripción (tu curiosidad)
        color=color_int  # Color del borde del embed
    )
    embed.set_image(
        url="https://yt3.googleusercontent.com/8-ce7p9udKhfyTpEtsNzvVLEZB4GfjVXz93IHzhZ0NtN0ozM3IvtlzSpHH0F150u_SFFqxqTuw=s176-c-k-c0x00ffffff-no-rj")
    await ctx.send(embed=embed)

@client.command()
async def agregarCuriosidad(ctx, *, curiosidad: str = None):
    if curiosidad is None:
        await ctx.send("Tenes que pasar la curiosidad para agregarla.")
        return
    if(ctx.author.id != 428678533263392772):
        await ctx.send("No tienes permiso para usar este comando")
        return
    # Leer el archivo para determinar el número de la próxima curiosidad
    with open("curiosidadJapones.txt", "r", encoding="utf-8") as file:
        curiosidades = file.readlines()
    # Determinar el número de la próxima curiosidad
    numero_nuevo_curiosidad = len(curiosidades) + 1
    # Agregar la nueva curiosidad al final del archivo
    with open("curiosidadJapones.txt", "a", encoding="utf-8") as file:
        file.write(f"{numero_nuevo_curiosidad}. {curiosidad}\n")

    # Enviar un mensaje de confirmación
    await ctx.send(f"Curiosidad agregada: {numero_nuevo_curiosidad}. {curiosidad}")

@client.command()
async def h(ctx):
    # url = 'https://api.lolicon.app/setu/v2'
    url = 'https://api.lolicon.app/setu/v2?tag=%E8%90%9D%E8%8E%89&r18=0&size=small'

    with open("mensajesHot.txt", "r", encoding="utf-8") as file:
        mensajesHot = file.readlines()
    i = random.randint(0, len(mensajesHot) - 1)

    async with aiohttp.ClientSession() as session:

        async with session.get(url) as response:

            if response.status == 200:
                data = await response.json()
                imagen = data["data"][0]["urls"]["small"]
                color_int = 16711680
                embed = discord.Embed(
                    title="Andas hot?",  # Título del embed
                    description=mensajesHot[i],  # Descripción
                    color=color_int  # Color del borde del embed
                )
                embed.set_image(url=imagen)
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Error en la petición: {response.status}")

@client.command()
async def agregarH(ctx, *, mensaje: str = None):
    if mensaje is None:
        await ctx.send("Tienes que pasar el mensaje para agregarlo.")
        return
    if ctx.author.id != 428678533263392772:  # Reemplaza con el ID del usuario permitido
        await ctx.send("No tienes permiso para usar este comando")
        return
    # Leer el archivo para determinar el número del próximo mensaje
    with open("mensajesHot.txt", "r", encoding="utf-8") as file:
        mensajes = file.readlines()
    # Determinar el número del próximo mensaje
    numero_nuevo_mensaje = len(mensajes) + 1
    # Agregar el nuevo mensaje al final del archivo
    with open("mensajesHot.txt", "a", encoding="utf-8") as file:
        file.write(f"{numero_nuevo_mensaje}. {mensaje}\n")

    # Enviar un mensaje de confirmación
    await ctx.send(f"Mensaje agregado: {numero_nuevo_mensaje}. {mensaje}")

@client.command()
async def buscarPersonaje(ctx, *, personaje: str):
    pass

@client.command()
async def buscarPalabra(ctx, *, palabra: str):
    url = "https://jotoba.de/api/search/words"
    data = {
        "query": palabra,
        "language": "Spanish",
        "no_english": True
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            if response.status == 200:
                response_json = await response.json()
            else:
                await ctx.send(f"Error en la solicitud: {response.status}")
                return

    # Extraer datos
    kanji_data = response_json.get('kanji', [{}])[0]
    word_data = response_json.get('words', [{}])[0]
    primer_kanji_literal = kanji_data.get("literal", "No disponible")
    primer_glosses = ', '.join(word_data.get("senses", [{}])[0].get("glosses", ["No disponible"]))
    
    # Verificar si hay una URL de audio
    audio_url = word_data.get("audio")
    if audio_url:
        audio_url = "https://jotoba.de" + audio_url
        view = AudioButton(audio_url)  # Crear la vista con el botón si hay audio
    else:
        view = None  # No crear la vista si no hay audio

    # Crear el embed
    embed = discord.Embed(title=f"Resultado para: {palabra}", color=0xDEADBF)
    embed.add_field(name="Kanji", value=primer_kanji_literal, inline=False)
    embed.add_field(name="Significado", value=primer_glosses, inline=False)

    # Enviar el embed con o sin el botón
    await ctx.send(embed=embed, view=view)

client.run(token_1.token())
