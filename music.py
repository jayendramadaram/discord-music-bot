import discord
from discord.ext import commands
from discord import FFmpegPCMAudio, PCMVolumeTransformer
import youtube_dl
import ffmpeg
import urllib.request
from bs4 import BeautifulSoup
import re

class music(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("You're not in a voice channel!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self,ctx,url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':"bestaudio" , "--default-search":"ytsearch"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            print()
            print()
            print(url2)
            print()
            print()
            source = await discord.FFmpegPCMAudio(url2, **FFMPEG_OPTIONS)
            vc.play(source)
    
    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.channel.send("Paused ⏸")
    
    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.channel.send("resume ⏯")

def setup(client):
    client.add_cog(music(client))