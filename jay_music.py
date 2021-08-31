import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

TOKEN = "ODgyMTc1MjE2OTU1MDU2MTU4.YS3jsQ.3EV_PVldTnHKUAR7a78w29GoWW0"
client.run(TOKEN)
