import test
import discord
from discord.ext.commands import Bot
from db_commands import Database
import markov_new as markov
import transformer_chatbot as tc
BOT_PREFIX = ("?", "!")
BOT_NAME = 'Emoma'
TOKEN = "NjA1NTMxMjc1NjU0MDcwMjc0.XUABuQ.e8iaRNS7Mxa6PThW6KIvYfmAt40"


client = Bot(command_prefix=BOT_PREFIX)
db = Database()
db.setup()

@client.event
async def on_ready():
    game = discord.Game("mind games with you!")
    await client.change_presence(status=discord.Status.idle, activity=game)


def ordered(string, words):
    string = string.lower()
    try:
        string.index(words)
        return True
    except:
        return False

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('!') or message.attachments:
        return
    elif BOT_NAME in message.content.lower() or ordered(message.content, words='how are you?'):
        await message.channel.send("Depends, we'll see")
    elif BOT_NAME in message.content.lower() or ordered(message.content, words='your name'):
        await message.channel.send("My name is Emoma")

    elif BOT_NAME in message.content.lower() or ordered(message.content, words='is my name') or ordered(message.content, words='my name'):
        await message.channel.send("Pretty sure your name is " + message.author.name)

    elif message.content.startswith('addnew'):
        f = open(message.author.name, "r")
        q = f.readlines()[0]
        f.flush()
        f.close()
        a = message.content
        a = a.split(' ', 1)[1]
        db.add_item(a)
        tc.lc.add_new(q, a)
        await message.channel.send("gotcha")
    elif BOT_NAME in message.content.lower() or client.user.mentioned_in(message):
        message_received = message.content
        message_received = message_received.split(' ', 1)[1]

        f = open(message.author.name, "w+")
        f.write(message_received)
        f.flush()
        f.close()

        db.add_item(message_received)
        response = markov.markov(message_received)
        #   markov = markov_old.Markov()
        #   response = markov.create_chain(BOT_NAME, message.content)
        await message.channel.send(response)
    else:
        await message.channel.send("Don't forget to tag me first!")
print("running")
client.run(TOKEN)