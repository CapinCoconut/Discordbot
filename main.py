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

# sends a message to new user in discord channel
@client.event
async def on_member_join(member):
    
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f'welcome to the server' + {member.mention})

#Let's the server know SRB is ready to use
@client.event
async def on_ready():
    general_channel = client.get_channel(805505983161827372)
    await general_channel.send('SRB has arrived!')


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

maybe = [
    'Make up your mind',
    'I do not have all day, hurry up and decide',
    'Go ask someone else then',
    'Stop waisting my time',
    'Venmo me $5 and I will give you an apology'
]

# random on_message events

@client.event
async def on_message(message):

    if message.content.startswith('!help'):
         general_channel = client.get_channel(805505983161827372)
         myEmbed = discord.Embed(title='SRB Current Version', description='SRB Version 1.1', color=0xFF0000)
         myEmbed.add_field(name='Version:', value='1.1', inline=False)
         myEmbed.add_field(name='Date Premiered', value='May 12, 2021', inline=False)
         myEmbed.set_author(name='Shawn Humphries')
         myEmbed.set_footer(text='This bot does a lot of random things, I have no idea what I am doing...but I am having fun')

         await general_channel.send(embed=myEmbed)

    if message.content.startswith('Hey SRB'):
        await message.channel.send('Do you need an apology?')
    if message.content.startswith('!yes'):
        await message.channel.send(random.choice(apologies))
        time.sleep(3)
        await message.channel.send('Would you like another apology?')
    if  message.content.startswith('!no'):
        await message.channel.send(random.choice(denials))
    if message.content.startswith('!thanks'):
        await message.channel.send(random.choice(replies))
    if message.content.startswith('!maybe'):
        await message.channel.send(random.choice(maybe))
    
    # message to play "what are the odds"

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