import discord
import nmap
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="[", help_command=None, intents=intents)

nmScan = nmap.PortScanner()

@bot.event
async def on_ready():
    print("Bot is ready!")

@bot.command()
async def kill(ctx):
  ip = ctx.message.content.split()[1]

  await ctx.send(f"> กำลังแสกน IP : `{ip}` Port `tcp` Pls รอหนูแปปนะไอสัสเครื่องช้า")

  try:
    nmScan.scan(ip, '21-443')
  except:
    await ctx.send(f"> {ip} พ่องอ่าาาาหนูหาHostไม่เจอ;w;")
    return

  for host in nmScan.all_hosts():
      print('Host : %s (%s)' % (host, nmScan[host].hostname()))
      print('State : %s' % nmScan[host].state())
      for proto in nmScan[host].all_protocols():
           print('----------')
           print('Protocol : %s' % proto)
 
           lport = list(nmScan[host][proto].keys())
           lport.sort()
           for port in lport:
            await ctx.send('> port : %s\tstate : %s' % (port, nmScan[host][proto][port]['state']))

  try:                
    await ctx.send('> State : %s' % nmScan[host].state())
  except:
    await ctx.send(f"> {ip} พ่องอ่าาาาหนูหาHostไม่เจอ;w;")
    return

bot.run(TOKEN)