@client.event
async def on_message(message):
    if message.content.lower() == "[komut-ismi]":
        await client.add_reaction(message, [istediginiz-emoji])
