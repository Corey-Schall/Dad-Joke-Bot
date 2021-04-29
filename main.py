import discord
import os
import requests
import json
from keep_alive import keep_alive

def get_joke():
  response = requests.get("https://icanhazdadjoke.com/slack")
  #response = requests.get("https://api.kanye.rest")
  json_data = json.loads(response.text)
  joke = json_data['attachments'][0]['text']
  #joke = json_data['quote']
  return(joke)

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$joke'):
    joke = get_joke()
    await message.channel.send(joke)

  if message.content.startswith("I'm hungry") or message.content.startswith("Im hungry") or message.content.startswith("im hungry"):
    await message.channel.send("Hi, hungry.  I'm Dad Joke Bot!")

  if message.content.startswith("I'm tired") or message.content.startswith("Im tired") or message.content.startswith("im tired"):
    await message.channel.send("Hi, tired.  I'm Dad Joke Bot!")
 


keep_alive()
client.run(os.getenv('TOKEN'))