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
