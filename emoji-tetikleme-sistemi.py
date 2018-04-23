@client.event
async def on_message(message):
    if message.content.lower() == prefix+"oyla":
        msg = await client.send_message(message.channel, 'Bu mesajı beğenin yada beğenmeyin.')
        kis = await client.wait_for_reaction(['👍', '👎'], message=msg) # İlk kısımı isterseniz yazmayın.
        await client.send_message(message.channel, '{0.user}kullanıcısı {0.reaction.emoji} oyunu verdi!'.format(kis))# yapılacaklar.
