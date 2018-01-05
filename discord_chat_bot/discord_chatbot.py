#!/usr/bin/env python3
# discord chatbot - 100 days of code day 2

import asyncio
import creds
import logging
import discord

# from https://discordpy.readthedocs.io/en/latest/logging.html#logging-setup
# enable DEBUG mode logging and output to a file named discord.log
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

'''
@asyncio.coroutine
def main_task():
    yield from client.login(creds.bot_token)
    yield from client.connect()
'''

'''
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main_task())
except:
    loop.run_until_complete(client.logout())
finally:
    loop.close()
'''

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(creds.bot_token)
