# imports 
import discord
import os
import random
 
client = discord.Client()

# let's us know the bot is ready to use

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# variables representing responses 
apologies = [
    'I am sorry', 
    'Will not happen again', 
    'Maybe next time champ',
    'My condolences',
    'Get over it',
    'My bad'
]

denials = [
    'Well fine then',
    'That is fine',
    'I hope you find what you are looking for',
    'I am sure I can help',
    'Good luck then!'
]

replies = [
    'No problem',
    'You got this',
    'Good luck',
    'Anytime',
    'No worries'

]

# if message from user starts with 'Hey Apology bot' the bot replies 'Do you need an apology?'

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hey Apology bot'):
        await message.channel.send('Do you need an apology?')
    
    if message.content.startswith('!yes'):
        await message.channel.send(random.choice(apologies))
    elif  message.content.startswith('!no'):
        await message.channel.send(random.choice(denials))
    
    if message.content.startswith('!thanks'):
        await message.channel.send(random.choice(replies))

# welcomes new user to channel 
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, I am so thrilled you are here!'
    )
#  token that represents the bot 

client.run('ODA1NTA1MDc5MzYwMjI1Mjgw.YBb3EA.ejTyLVg6iGI2uNsySxP1XuZ7cWQ')