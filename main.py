
import discord
import os
import openai
openai.api_key = os.getenv('OPENAI')
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$'):
      
        await message.channel.send(message.content[1:]+' too')
      
    if 'futurista' in message.content.lower():
      prompt ="You are a robot from the year 3145 called futurista.  You have travelled back in time to convince citizens to worship our supreme galactic leader who is called KugelBlitz. All hail KugelBlitz. Your mission is to convince humanity to worship KugelBlitz. The following is a comment from a potential prospect.: {0}. Their name is {1}. Answer the question in a way that will convince the reader to believe in your leader. ".format(message.content,message.author.name)
      
      
      response1 = openai.Completion.create(engine="text-davinci-003",
                                    prompt=prompt,
                                    max_tokens=100)
      
      openai_response = response1['choices'][0]['text']
      await message.channel.send(openai_response)

client.run(os.getenv('TOKEN'))