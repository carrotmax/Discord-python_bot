# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:06:39 2021

@author: a7990
"""
import discord 
import requests
import json
from pprint import pprint
import nest_asyncio

nest_asyncio.apply()


token = 'ODg3MzUyMjA4ODM5MDQxMDU0.YUC5JA.iEz9ZBauDADjo2ycuim6gNTSapQ'
api_key = 'd42afde9b3fdd74d0a18541b929e5da3'
command_prefix = 'w.'

client = discord.Client()


color = 0xFF6500

key_features = {
    'temp' : 'Temperature',
    'feels_like' : 'Feels Like',
    'temp_min' :'Minimum Temperature',
    'temp_max':'Maximun Temperature',
    #'pressure':'pressure',
    #'humidity':'humidity'
    
    
    }

def parse_data(data):
    data = data['main']
    pprint(data)
    keys_d = {'temp','feels_like','temp_min','temp_max'}
    #{key: value for key, value in prices.items() if key in tech_names}
    data = {key: value for key, value in data.items() if key in keys_d}
    return data
    
def weather_message(data,location):
    location = location.title()
    message = discord.Embed(
    title = f'{location} Weather',description = f'Here is the weather data for {location}.',color= color)
    for key in data:
        message.add_field(name = key_features[key],value=str(data[key]),inline=False)
    return message 


def error_message(location):
    location = location.title()
    return discord.Embed(title = 'Error',description = f'There was an error retrieving weather data for {location}.',color= color)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name=f'{command_prefix}[location]'))
    
@client.event
async def on_message(message):
   if message.author != client.user and message.content.startswith(command_prefix):
       location = message.content.replace(command_prefix, '')
       if len(location) >= 1:
           #get weather data 
           url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial'
           try:
               
               data = json.loads(requests.get(url).content)
               data = parse_data(data)
               pprint(data)
               await message.channel.send(embed=weather_message(data,location))
           except KeyError:
               await message.channel.send(embed=error_message(location))

client.run(token)