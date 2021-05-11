# imports 
import discord
import os
import random
import time
from discord.ext import commands


client = discord.Client()

# let's us know the bot is ready to use
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f'welcome to the server' + {member.mention})

@client.event
async def on_member__remove(member):
    print(f'{member} has departed the server.')


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
    if message.content.startswith('Hey Apology bot'):
        await message.channel.send('Do you need an apology?')
    
    if message.content.startswith('!yes'):
        await message.channel.send(random.choice(apologies))
    elif  message.content.startswith('!no'):
        await message.channel.send(random.choice(denials))
    
    if message.content.startswith('!thanks'):
        await message.channel.send(random.choice(replies))
    
    if message.content.startswith('what are the odds?'):
        await message.channel.send("Congratulations! You have started 'What Are the Odds! Follow the next steps. There is No going back now!")
        time.sleep(4)
        await message.channel.send('Think of a number between 1 and 10')
        time.sleep(5)
        await message.channel.send('Type that number in 3')
        time.sleep(5)
        await message.channel.send('2')
        time.sleep(5)
        await message.channel.send('1')
        time.sleep(3)
        await message.channel.send('Now')
        time.sleep(1)
        await message.channel.send(random.randint(1,10))

#  token that represents the bot 

client.run('ODA1NTA1MDc5MzYwMjI1Mjgw.YBb3EA.ejTyLVg6iGI2uNsySxP1XuZ7cWQ')