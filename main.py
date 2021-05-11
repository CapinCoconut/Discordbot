# imports 
import discord
import os
import random
import time
from discord.ext import commands

client = commands.Bot(command_prefix='--')

@client.command(name='version')
async def version(context):
    general_channel = client.get_channel(805505983161827372)
        
    myEmbed = discord.Embed(title='SRB Current Version', description='SRB Version 1.1', color=0xFF0000)
    myEmbed.add_field(name='Version:', value='1.0.1', inline=False)
    myEmbed.add_field(name='Date Premiered', value='May 12, 2021', inline=False)
    myEmbed.set_author(name='Shawn Humphries')
    myEmbed.set_footer(text='This bot does some of random things, I have no idea what I am doing...but I am having fun')
    myEmbed.set_image(url='https://pixelartmaker-data-78746291193.nyc3.digitaloceanspaces.com/image/4676fd82ca5fa1c.png')
    myEmbed.set_thumbnail(url='https://i.imgflip.com/4a84il.png')
    await context.message.channel.send(embed=myEmbed)

#shows how many users are in the discord channel (including the bot)
@client.command(aliases=["mc"])
async def member_count(ctx):

    a=ctx.guild.member_count
    b=discord.Embed(title=f"members in {ctx.guild.name}",description=a,color=discord.Color((0xFF)))
    await ctx.send(embed=b)
    
# let's us know the bot is ready to use
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    general_channel = client.get_channel(805505983161827372)
    await general_channel.send("SRB (Shawn's Random Bot) has arrived!")

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

    if message.content.startswith('Hey SRB'):
        await message.channel.send('Do you need an apology?')
    if message.content.startswith('--yes'):
        await message.channel.send(random.choice(apologies))
        time.sleep(3)
        await message.channel.send('Would you like another apology?')
    if  message.content.startswith('--no'):
        await message.channel.send(random.choice(denials))
    if message.content.startswith('--thanks'):
        await message.channel.send(random.choice(replies))
    if message.content.startswith('--maybe'):
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

#sends a message to new user in discord channel
# async def on_member_join(member):
#     await message.channel.send(f"{member.mention}'Welcome to the Test server, we do just test myself for now!'")
    
    await client.process_commands(message)

#  token that represents the bot 

client.run('ODA1NTA1MDc5MzYwMjI1Mjgw.YBb3EA.ejTyLVg6iGI2uNsySxP1XuZ7cWQ')