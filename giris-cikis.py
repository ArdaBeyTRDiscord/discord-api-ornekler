import discord

client = discord.Client()

@client.event
async def on_member_join(member):
  kanal = discord.utils.get(member.server.channels, name="mod-log")
  await client.send_message(kanal, "{} katıldı :tada:".format(member.mention))
@client.event
async def on_member_leave(member):
  kanal = discord.utils.get(member.server.channels, name="mod-log")
  await client.send_message(kanal, "`{}` aramızdan ayrıldı...".format(member))
  
