# Roody Discord Bot | Rude Discord Bot
# Ported to Python by @gabedev

import bs4
import discord
import urllib.request
import asyncio

client = discord.Client()

def get_insult():
    sock = urllib.request.urlopen('http://insultgenerator.org')
    html = sock.read()
    soup = bs4.BeautifulSoup(html, 'html.parser')
    for insult_str in soup.find_all('div', {'class': 'wrap'}):
        insult = insult_str.get_text()
        insult = insult.replace('\n', '').replace('\r', '')
        return (insult)

@client.event
async def on_ready():
    print ('Logged on as: {0}'.format(client.user))

@client.event
async def on_message(message):
    if client.user.mention in message.content:
        await client.send_message(message.channel, '{0}, {1}'.format(message.author.mention, get_insult()))


client.run('token')
