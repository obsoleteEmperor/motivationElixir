import discord
from discord.ext import commands 
import os
import requests
import json
import string
import random
from replit import db
from keep_alive import keep_alive
import io
import aiohttp  #Asynchronous HTTP Client to get something from the web, like an image

client = commands.Bot(command_prefix = ",", case_insensitive=True, help_command=None)     #Creates a connection to our bot. Parameters: Enables the bot command prefix, turned off the case sensitivity of the commands and also turned off the default help command to write our own custom help command

#Functions made by us
#Functions made by us
#Text functions
def get_quote():                                #(F_001)           #Funtion to get the quotes using an API
  response_quote = requests.get("https://zenquotes.io/api/random")
  json_data_quote = json.loads(response_quote.text)
  quote = "> **`" + json_data_quote[0]['q'] + "  -" + json_data_quote[0]['a']+ "`**"
  return(quote)

def get_anime_quote():                          #(F_002)           #Funtion to get the anime quotes using an API
  response_anime_quote = requests.get("https://animechan.vercel.app/api/random")
  json_data_anime_quote = json.loads(response_anime_quote.text)
  anime_quote = "> **`" + json_data_anime_quote['quote'] + "  -" + json_data_anime_quote['character'] + "    Anime: " + json_data_anime_quote['anime'] + "`**"
  return(anime_quote) 

def get_office_quote():                        #(F_003)           #Function to get The Office Quotes using an API 
  office_quotes_response = requests.get('https://officeapi.dev/api/quotes/random')
  json_office_quotes = json.loads(office_quotes_response.text)
  office_quote = "> **`" + json_office_quotes['data']["content"] + "`**" + "\n > **` -" + json_office_quotes["data"]["character"]["firstname"] + " "  + json_office_quotes["data"]["character"]["lastname"] + "`**" 
  return(office_quote)

def get_prg_quote():                            #(F_004)           #Function to get  Programming Quotes using an API   
  prg_quote_response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
  json_prg_quote = json.loads(prg_quote_response.text)
  prg_quote = "> **`" + json_prg_quote["quote"] + "`**" + "  -**" + json_prg_quote["author"] + "**"
  return(prg_quote)

def get_affirmation():                         #(F_005)            #Function to get Affirmation using an API
  affirmation_response = requests.get('https://www.affirmations.dev/')
  json_affirmation = json.loads(affirmation_response.text)
  affirmation = "> **`" + json_affirmation['affirmation'] + ".`**" 
  return(affirmation)

def get_zlatan_quote():                       #(F_006)             #Function to get Zlatan Ibrahimovic Jokes using an API
  response_zlatan_quote = requests.get("http://www.zlatanjokes.site/joke")
  json_data_zlatan_quote = json.loads(response_zlatan_quote.text)
  zlatan_quote = "> **`" + json_data_zlatan_quote['joke'] + "`**"
  return(zlatan_quote)

def get_chuck_quote():                       #(F_007)              #Function to get Chuck Norris Jokes using an API
  response_chuck_quote = requests.get("https://api.chucknorris.io/jokes/random")
  json_data_chuck_quote = json.loads(response_chuck_quote.text)
  chuck_quote = "> **`" + json_data_chuck_quote['value'] + "`**"
  return(chuck_quote)

def get_joke_punchline():                    #(F_008)              #Function to get Joke Puchlines using an API
  joke_punchline_response = requests.get('https://official-joke-api.appspot.com/random_joke')
  json_joke_punchline = json.loads(joke_punchline_response.text)
  joke_punchline = "> **`" + json_joke_punchline['setup'] + "`** " + "\n \n" + "||**`" + json_joke_punchline['punchline'] + "`**||"
  return(joke_punchline)


#Image Functions
def get_random_dog_pics():                   #(F_501)              #Function to get the url of the dog picture using an API
  random_dog_pic_response = requests.get("https://dog.ceo/api/breeds/image/random")
  random_dog_pic_json = json.loads(random_dog_pic_response.text)
  random_dog_pic_url = random_dog_pic_json['message']
  return(random_dog_pic_url)

def get_random_cat_pics():                   #(F_502)               #Function to get the url of the cat picture using an API
  random_cat_pic_response = requests.get('https://api.thecatapi.com/v1/images/search')
  random_cat_pic_json = json.loads(random_cat_pic_response.text)
  random_cat_pic_url = random_cat_pic_json[0]["url"]
  return(random_cat_pic_url)

def get_quoted_img():                        #(F_503)               #Function to get the url of the quoted image using an API
  random_quoted_response = requests.get('https://inspirobot.me/api?generate=true')    #Opens the url
  random_quoted_pic_url = random_quoted_response.content                              #Gets the conetents of the webpage
  return(random_quoted_pic_url.decode('utf-8'))                                       #Content of the webapge is in byte string, so we convert it






#Command definitions
#Command definitions
@client.event                         					#event decorator, registers an event
async def on_ready():														#callback function that is triggered once bot is online(ready to use)
  await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name= ', commands'))     #To set the bot status and to set it's activity
  print('We have logged in as {0.user}'.format(client))

@client.command()                      #This command displays the function of each and every command provided by out bot
async def help(ctx):                   #Turned off the default help() to write this custom one
  embed=discord.Embed(title="Bot Commands", description="A list of all bot commands. Use a **`,`** as prefix to all these commands.", color=0x6b0ff5)
  embed.add_field(name="quote famous", value="Displays  quotes from famous people:coin:", inline=True)
  embed.add_field(name="quote anime", value="Displays an anime quote:nazar_amulet:", inline=True)
  embed.add_field(name="quote office / the office", value="Displays a quote from The Office:man_office_worker:", inline=True)
  embed.add_field(name="quote prg / programming", value="Displays a :computer:programming quote", inline=True)
  embed.add_field(name="8ball / eightball (question)", value="Ask the :8ball: 8 Ball a question you want answered", inline=False)
  embed.add_field(name="ping", value="Displays the bot's ping in ms:chart_with_upwards_trend:", inline=True)
  embed.add_field(name="motivate / affirmation", value="Motivates you :smile:", inline=True)
  embed.add_field(name="zlatan / ibra / ibrahimovic", value="Replies with a Zlatan joke:soccer:", inline=False)
  embed.add_field(name="chuck / norris", value="Replies with a Chuck Norris joke:cowboy:", inline=True)
  embed.add_field(name="joke / punchline", value="Replies with a punchline:punch: joke", inline=True)
  embed.add_field(name="dogs / doggie / dog", value="Displays a pic of dog/dogs:dog:", inline=True)
  embed.add_field(name="cats / kitty / cat", value="Displays a pic of :heart_eyes_cat: cat/cats", inline=True)
  embed.add_field(name="inspire", value="Displays an image with an inspiring quote :strawberry:",inline=True)
  embed.set_footer(text="Motivation Elixir v2.1.1")
  await ctx.send(embed=embed)


@client.command()
async def ping(ctx):                                                 #Command to return latency of the bot
  await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command(aliases = ["8ball","eightball"])                     #aliases of the 8ball command
async def _8ball(ctx, *, question):
  responses = ["It is certain.", 
              "It is decidedly so.",
              "Without a doubt.",
              "Yes - definitely.",
              "You may rely on it.",
              "As I see it, yes.",
              "Most likely.",
              "Outlook good.",
              "Yes.",
              "Signs point to yes.",
              "Reply hazy, try again.",
              "Ask again later.",
              "Better not tell you now.",
              "Cannot predict now.",
              "Concentrate and ask again.",
              "Don't count on it.",
              "My reply is no.",
              "My sources say no.",
              "Outlook not so good.",
              "Very doubtful."]
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def quote(ctx, *, quote_option):                                                      #this command replies with a quote depending on the option
  quote_option = quote_option.lower()

  if quote_option == "famous":                                                              #replies with a random quote
    quote = get_quote()                                #(F_001)
    await ctx.send(quote)

  elif quote_option == "anime":                                                             #replies with an anime quote
    anime_quote = get_anime_quote()                    #(F_002)
    await ctx.send(anime_quote)

  elif (quote_option == "the office") or (quote_option =="office"):                         #replies with an Office quote
    office_quote = get_office_quote()                  #(F_003)                            
    await ctx.send(office_quote)

  elif(quote_option == "prg") or (quote_option == "programming"):                           #replies with a programming quote
    prg_quote = get_prg_quote()                        #(F_004)    
    await ctx.send(prg_quote)                        
  
@client.command(aliases = ["affirmation"])                                    
async def motivate(ctx):                                                                  #This command replies with an affirmation
  affirmation = get_affirmation()                     #(F_005)
  await ctx.send(affirmation)

@client.command(aliases = ["ibra" , "ibrahimovic"])                                                                         
async def zlatan(ctx):                                                                    #This command replies with a Zlatan joke
  zlatan_quote = get_zlatan_quote()                   #(F_006)
  await ctx.send(zlatan_quote)

@client.command(aliases = ["chuck"])
async def norris(ctx):                                                                   #This command replies with a Chuck Norris jokes
  chuck_quote = get_chuck_quote()                    #(F_007)
  await ctx.send(chuck_quote)                 

@client.command(aliases = ["punchline"])
async def joke(ctx):                                                                     #This command replies with a Joke Punchline
  joke_punchline = get_joke_punchline()              #(F_008)
  await ctx.send(joke_punchline)

@client.command(aliases = ["doggie", "dog"])
async def dogs(ctx):                                                                     #This command replies with a pic of a dog/dogs
  dog_pic_url = get_random_dog_pics()                #(F_501)                    #stores the image http url
  dog_pic_name = str(dog_pic_url)                                              #displays the url for user
  async with aiohttp.ClientSession() as session:
    async with session.get(dog_pic_url) as resp:
        if resp.status != 200:                                                 #checks if the HTTP Status code is 200 to ensure we get our image
          return await ctx.send('Facing techinal difficulty at the moment, try again later.')
        data = io.BytesIO(await resp.read())                                   #A binary stream using an in-memory bytes buffer, to send the image                   
        await ctx.send(file=discord.File(data, dog_pic_name))

@client.command(aliases = ["kitty","cat"])
async def cats(ctx):                                                                     #This command replies with a pic of a cat/cats
  cat_pic_url = get_random_cat_pics()               #(F_502)
  cat_pic_name = str(cat_pic_url)                         
  async with aiohttp.ClientSession() as session:          #We have a ClientSession called session 
    async with session.get(cat_pic_url) as resp:          #ClientResponse object called resp
      if resp.status != 200:                            #checks if the HTTP Status code is 200 to ensure we get our image
        return await ctx.send('Facing techinal difficulty at the moment, try again later.')
      data = io.BytesIO(await resp.read())              #A binary stream using an in-memory bytes buffer, to send the image                   
      await ctx.send(file=discord.File(data, cat_pic_name)) 

@client.command()
async def inspire(ctx):                                                                  #This command replies with a pic of inspiration
  quoted_pic_url = get_quoted_img()                #(F_503)    
  quoted_pic_name = str(quoted_pic_url)
  async with aiohttp.ClientSession() as session:          #We have a ClientSession called session 
    async with session.get(quoted_pic_url) as resp:          #ClientResponse object called resp
      if resp.status != 200:                            #checks if the HTTP Status code is 200 to ensure we get our image
        return await ctx.send('Facing techinal difficulty at the moment, try again later.')
      data = io.BytesIO(await resp.read())              #A binary stream using an in-memory bytes buffer, to send the image                   
      await ctx.send(file=discord.File(data, quoted_pic_name)) 

keep_alive()                         #To keep the server up and running
client.run(os.getenv('TOKEN'))       #token/password of our bot to run the bot. We are hiding our token from the public