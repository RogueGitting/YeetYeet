import discord
from discord.ext import commands
import random

client = discord.Client()
embed = discord.Embed

@client.event
async def on_message(message):
    # NO-REPLY
    if message.author == client.user:
        return
    elif message.author.id == "356355137641512961" or message.author.id == "301280327916191744":
        return
    else:
        print("Message Received from "+message.author.name)
    if message.content.startswith("+rpstanroll"):
        ran = random.randint(1,12)
        await client.send_message(message.channel, ":game_die: You rolled {}".format(ran))
    if message.content.startswith("+rp6maxroll"):
        ran = random.randint(1,6)
        await client.send_message(message.channel, ":game_die: You rolled {}".format(ran))
    if message.content.startswith("+help"):
        embed = discord.Embed(title=":robot: **RogueBot help**", color=discord.Colour(0xAA00FF))
        embed.add_field(name="Roleplay commands", value="`+rpstanroll` for a 1-12 dice roll, `+rp6maxroll` for a 1-6 dice roll.")
        embed.add_field(name="Other commands", value="`+credits` for the credits.")
        embed.set_footer(text="RogueBot | Help- | Bot by @Rogue#3744")
        await client.send_message(message.author, embed=embed)
    if message.content.startswith("+credits"):
        embed = discord.Embed(title=":robot: RogueBot Credits", color=discord.Colour(0xFF8800))
        embed.add_field(name="Lead Developer", value="@Rogue#3744")
        embed.set_footer(text="RogueBot | Help-Credits | Bot by @Rogue#3744")
        await client.send_message(message.author, embed=embed)
    #if message.content.startswith("+randcolor"):
        
        #red = hex(random.randint(0,255)).split('x')[-1]
        #print(red)
        #green = hex(random.randint(0,255)).split('x')[-1]
        #print(green)
        #blue = hex(random.randint(0,255)).split('x')[-1]
        #print(blue)
        #rgb = "0x"+red+green+blue
        #print(rgb)
        #embed = discord.Embed(title="Random Colour", color=discord.Colour(rgb))
        #await client.send_message(message.author, embed=embed)


@client.event
async def on_ready():
    print('Logged in as'+" "+client.user.name+" or "+client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='RogueBot | +help for help.'), status=discord.Status.dnd, afk=False)
    #while True:
    #red = hex(random.randint(0,255)).split('x')[-1]
    #print(red)
    #green = hex(random.randint(0,255)).split('x')[-1]
    #print(green)
    #blue = hex(random.randint(0,255)).split('x')[-1]
    #print(blue)
    #rgb = "0x"+red+green+blue
    #print(rgb)
    #print("Activate")
client.login('MzU2MzU1MTM3NjQxNTEyOTYx.DLRghg.a_C-K_lIe3NQgVZrB6-sRI0cwB8')
