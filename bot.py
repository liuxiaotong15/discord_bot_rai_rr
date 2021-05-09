from discord.ext import tasks
import discord
import random
import requests
import json


url = 'https://subgraph.reflexer.finance/subgraphs/name/reflexer-labs/rai' 
payload = json.dumps({"query":"{systemStates{currentRedemptionRate{annualizedRate}}}","variables":None,"operationName":None})

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        self.my_background_task.start()


    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')
        
        # if message.content.startswith('$change_name'):
        #     await message.guild.me.edit(nick='RR_{0}%'.format(random.random()))
        # print('Message from {0.author}: {0.content}'.format(message))

    @tasks.loop(seconds=60) # task runs every 60 seconds
    async def my_background_task(self):
        resp = requests.post(url=url, data=payload)
        data = resp.json() # Check the JSON Response Content documentation below
        print(data, type(data))
        rr = data['data']['systemStates'][0]['currentRedemptionRate']['annualizedRate']
        print(rr)

        rr = (float(rr)-1) * 100
        if client.user == None:
            return
        
        for guild in client.guilds:
            await guild.me.edit(nick='RR_{0:.4f}%'.format(rr))

client = MyClient()
client.run('ODQwODI5NzMwNzc3MzMzNzgw.YJd5tQ.RnJ8fFK0jIb8OjAdux4IlKiXQZE')
