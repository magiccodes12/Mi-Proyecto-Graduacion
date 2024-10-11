import discord
import random
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$check"):
        if message.attachments:
            for attachment in message.attachments:
                # Guarda el archivo adjunto en la carpeta actual
                await attachment.save(f"./{attachment.filename}")
                await message.channel.send(f"Guarda la imagen en ./{attachment.filename}")
        else:
            await message.channel.send("Olvidaste subir la imagen.")

    if message.content.startswith("$Muestrame imagenes de la contaminacion"):
        try:
            # Selecciona aleatoriamente un archivo de la carpeta 'images'
            img_name = random.choice(os.listdir('images'))
            with open(f'images/{img_name}', 'rb') as f:
                picture = discord.File(f)
            # Envía la imagen al canal
            await message.channel.send(file=picture)
        except FileNotFoundError:
            await message.channel.send("No se encontró la carpeta 'images' o no hay imágenes disponibles.")
        except Exception as e:
            await message.channel.send(f"Hubo un error al mostrar la imagen: {e}")

    elif message.content.startswith("$Que es la contaminacion"):
        await message.channel.send(f'La contaminación es un problema que está afectando gravemente a nuestro planeta. En otras palabras, se refiere a las sustancias nocivas en el aire, agua o suelo. Esto puede ser muy dañino al medio ambiente, a los seres vivos y a nuestra salud. Debido a eso, es muy importante saber tomar medidas de precaución para mejorar nuestro futuro, como por ejemplo: reciclar, reducir y reutilizar.')
    
    elif message.content.startswith("$Clasifica residuos"):
        await message.channel.send(f"Hay 3 categorías principales: Residuos Reciclables: Son materiales que pueden ser reciclados y reutilizados para hacer nuevos productos. Por ejemplo botellas de plástico, latas de aluminio, periódicos, cartones limpios, y envases de vidrio. Es importante colocarlos en los contenedores correctos para que puedan ser recogidos y procesados correctamente. Residuos Orgánicos: Son desechos biodegradables, materiales que provienen de plantas o animales y se descomponen naturalmente. Los restos de comida y de jardinería entran en esta categoría. Pueden ser compostados para convertirse en abono para plantas. Residuos No Reciclables: Son materiales que no pueden ser reciclados o compostados y van a los vertederos. Esto incluye cosas como pañales o envases de comida, y algunos tipos de plásticos que no son aceptados por los programas de reciclaje locales. Es importante tratar de reducir su cantidad al mínimo y buscar alternativas más ecológicas.")
    
    elif message.content.startswith("$Hay algo mas que puedo hacer"):
        await message.channel.send(f"Algo más podría ser que si tienes objetos que ya no vayas a utilizar como jugetes, ropa o mantas, no los deseches. Se los puedes regalar a personas pobres o en malas condiciones que probablemente lo necesiten más que tú. Esto puede ayudar extendiendo la vida útil de muchos recursos y evitar la fabricación de nuevos.")
    
    elif message.content.startswith("$Tipos de contaminacion"):
        await message.channel.send(f"Los principales tipos son: Contaminación del aire: Cuando los humos de fabricas o gases de auto ensucian el aire. Contaminación del agua: Cuando los mares, rios o lagos, se ensucian con basura o diversos residuos. Contaminación del suelo: Cuando el suelo se contamina con basura o desperdicios.")

client.run()