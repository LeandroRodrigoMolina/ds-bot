import discord
from discord.ext import commands
import random
import token_1
# Creando un array en Python con 5 curiosidades sobre letras del japonés

curiosidades_japones = [
    "El japonés usa tres sistemas de escritura diferentes: Kanji, Hiragana y Katakana.",
    "Los Kanji son caracteres de origen chino y cada uno puede tener múltiples significados y pronunciaciones.",
    "Hiragana se usa principalmente para palabras gramaticales y para aquellos vocablos que no tienen un Kanji asociado.",
    "Katakana se emplea para palabras extranjeras, nombres propios, y para dar énfasis, similar al uso de cursivas en occidente.",
    "El japonés también utiliza el 'furigana', pequeños caracteres Hiragana o Katakana que se colocan junto a los Kanji para indicar su pronunciación."
]
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()
async def duda(ctx):
    i = random.randint(0, 4)
    # Crear un embed
    color_hex = "2E0B36"
    color_int = int(color_hex, 16)
    print("color", color_int)
    embed = discord.Embed(
        title="Curiosidad sobre el Japonés",  # Título del embed
        description=curiosidades_japones[i],   # Descripción (tu curiosidad)
        color=color_int  # Color del borde del embed (verde en este caso)
    )
    embed.set_image(url="https://yt3.googleusercontent.com/8-ce7p9udKhfyTpEtsNzvVLEZB4GfjVXz93IHzhZ0NtN0ozM3IvtlzSpHH0F150u_SFFqxqTuw=s176-c-k-c0x00ffffff-no-rj")
    await ctx.send(embed=embed)

client.run(token_1.token())