import discord
import requests
import json


client = discord.Client()

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0] ['q'] + '-' +    json_data[0] ['a']
    return(quote)



@client.event
async def on_ready():
    print("We have logged in sucessfully as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author==client.user:
        return

    msg = message.content

    if msg.startswith('%help'):
        await message.channel.send('Prefix is %\nCommands are:\n1.aks\n2.vebev\n3.ani\n4.prash\n5.prad\n6.quote')

    if msg.startswith('%quote'):
        await message.channel.send(get_quote())
    
    if msg.startswith('%aks'):
        await message.channel.send('DEPRESSUN')
    
    if msg.startswith('%vebev'):
        await message.channel.send('NUB')

    if msg.startswith('%ani'):
        await message.channel.send('YES YES YES YES YES')

    if msg.startswith('%prash'):
        await message.channel.send('PERO')

    if msg.startswith('%prad'):
        await message.channel.send('GOD of war')


client.run('NzU2MTAyMzU1NTg1MzM1Mjk2.X2M9MQ.0sJUiBAr-9WJ3Qc-q124W5t6XvI',bot=True)





































