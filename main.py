# imports 
import discord
import os
import random

client = discord.Client()

# let's us know the bot is ready to use
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        print (f'Hi {member.name}, welcome to my Discord server!')
    )
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

@client.event
async def on_message(message):
    if message.author == client.user:
         return
    
    chooser1 = None
    chooser2 = None
    asker1 = None

    if message.content.startswith('what are the odds?'):
        await message.channel.send("Enter a number you would like to play out of.... (1 out of....)")
        chooser1 = input()
        await message.channel.send('you picked 1 out of' + ' ' + chooser1)
        await message.channel.send('Asker: enter a number')
        asker1 = input()
        await message.channel.send('Chooser: enter a number')
        chooser2 = input()
    
    if chooser2 == asker1:
        await message.channel.send('You both picked ' + str(chooser2) + '!!!!')

        






# #  token that represents the bot 

client.run('ODA1NTA1MDc5MzYwMjI1Mjgw.YBb3EA.ejTyLVg6iGI2uNsySxP1XuZ7cWQ')