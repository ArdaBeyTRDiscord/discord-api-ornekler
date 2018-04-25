import discord

client = discord.Client()

@client.event
asnyc def on_message(message):
  if message.content.lower() == "deneme":
    await client.send_message(message.channel, "Adını gir:")
    msj = await client.wait_for_message(timeout=30, author=message.author, channel=message.channel)
    await client.send_message(message.channel, "İsmin {}".format(msj.content))
