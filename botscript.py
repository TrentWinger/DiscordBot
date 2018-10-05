
# Work with Python 3.6
import discord
import botlogic
import mastermind
import urllib.parse
import youtube_dl
import urllib.request
import bs4
import random

file = open("TOKEN.txt")
TOKEN = file.readline()

client = discord.Client()

players = {}

mmGames = [1]

#Within avatars, each key is a day of the week, with 0 being Monday, and 6 being Sunday.
avatars = {
    0:{'image': 'dedede.jpg', 'name': 'King BeepBeepBeep'},
    1:{'image': 'diddy.jpg', 'name': 'Diddy Droid'},
    2:{'image': 'donkey.jpg', 'name': 'Robo Kong'},
    3:{'image': 'duckhunt.jpg', 'name': 'Duck Bot'},
    4:{'image': 'senorgw(nobueno).jpg', 'name': 'Señor Game&Watch'},
    5:{'image': 'kirby.jpg', 'name': 'Kirbit'},
    6:{'image': 'falco.jpg', 'name': 'Falc0'}
}



@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!fall2018'):
        msg = 'The Fall 2018 semester is '+botlogic.percentFall2018()+'% over.'
        await client.send_message(message.channel, msg)

    if message.content.startswith('!rollcharacter'):
        msg = 'Here is your DnD character! \n\n'+botlogic.rollCharacter().format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!kingdedede'):
        await playAudio(message.author, 'https://www.youtube.com/watch?v=-KOlVl77SkQ&t=')

    if message.content.startswith('!denver'):
        await playAudio(message.author, 'https://www.youtube.com/watch?v=1vrEljMfXYo')

    if message.content.startswith('!stop'):
        await leave(message.author)

    if message.content.startswith('!play'):
        msg = message.content.format(message)
        arguments = msg.split(" ")
        reply = "" #Create a blank string to add to
        for x in arguments[1:]: #Skip the first element in the list
            reply += x+" " #Add each "word" from the message as a separate string
        final = searchVideo(reply) #Search for the given text on YouTube
        await client.send_message(message.channel, final) #Show video link in text chat
        await playAudio(message.author, final) #Play the audio

    if 'this is so sad' in message.content:
        await playAudio(message.author, searchVideo("Despacito"))

    if message.content.startswith('!rps'):
        msg = message.content.format(message)
        arguments = msg.split(" ")
        hand = arguments[1]
        reply = botlogic.rockPaperScissors(hand)+hand.format(message)

        await client.send_message(message.channel, reply)

    if message.content.startswith('hewwo?'):
        msg = "https://i.kym-cdn.com/entries/icons/original/000/024/221/upload.png"
        await client.send_message(message.channel, msg)

    if message.content.startswith('!mm'):
        msg = message.content.format(message)
        arguments = msg.split(" ")
        if mmGames[0] == None:
            mmGames[0] = mastermind.Game()
        if mmGames[0] != None:
            print("To be continued")

def searchVideo(request):

    search = urllib.parse.quote(request)
    print('Searching for: '+search)
    url = "https://www.youtube.com/results?search_query="+search
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = bs4.BeautifulSoup(html, "html.parser")
    soup.prettify()
    for anchor in soup.findAll('a', href=True): #Iterate through links found
        if(anchor['href']).startswith('/watch?v') and 'list=' not in anchor['href']: #Find "top" video and ignore playlists
            return ('https://www.youtube.com'+anchor['href'])

async def playAudio(author, url):
    await leave(author)
    await join(author)
    await play(author, url)

async def join(author):
    channel = author.voice.voice_channel
    await client.join_voice_channel(channel)

async def leave(author):
    for x in client.voice_clients:
        if(x.server == author.server):
            return await x.disconnect()

async def play(author, url):
    server = author.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()


@client.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    for x in avatars:
        if x == botlogic.checkDay():
            with open(avatars[x]['image'], 'rb') as f:
                await client.edit_profile(avatar=f.read())
                await client.edit_profile(username=avatars[x]['name'])
                print (avatars[x]['name']+' has been selected')


    print('------')

client.run(TOKEN)

