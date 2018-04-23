    if msg.startswith(pr+"yaz"):
        await client.delete_message(message)
        try:
            yazmalık = "".join(message.content.split(" ")[1])
            mbd = discord.Embed(title="Hey Ordakiler!:", description=yazmalık, color=random.randint(0, 0xFFFFFF))
            mbd.set_footer(text="{} Tarafından yazıldı.".format(message.author),icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=mbd)
        except:
            bdmsj = await client.send_message(message.channel, "**Yazmak istediğin şey anlaşılmadı!!**\nYazmak istediğin metini yaz, eğer yazmak istemiyorsan `çık` yaz.")
            msj = await client.wait_for_message(timeout=30, author=message.author, channel=message.channel)
            await client.delete_message(bdmsj)
            await client.delete_message(msj)
            yzm = msj.content
            if yzm.lower() == ("çık") or yzm.lower() == ("cik"):
                await client.send_message(message.channel, "Metin beklemesinden çıkıldı.")
            else:
                mbd = discord.Embed(title="Hey Ordakiler!:", description=yzm, color=random.randint(0, 0xFFFFFF))
                mbd.set_footer(text="{} Tarafından yazıldı.".format(message.author),icon_url=message.author.avatar_url)
                await client.send_message(message.channel, embed=mbd)
