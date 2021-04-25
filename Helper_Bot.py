import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='>', description='Bot de Ayuda')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def sum(ctx, num1: int, num2: int):
    await ctx.send(num1 + num2)

@bot.command()
async def mult(ctx, num1: int, num2: int):
    await ctx.send(num1 * num2)

@bot.command()
async def stats(ctx):
    embed = discord.Embed(title=f'{ctx.guild.name}', description='Lorem ipsum dolor sit amet', timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name='Servidor Creado el', value=f'{ctx.guild.created_at}')
    embed.add_field(name='Dueño Del Server', value='Drackord#6863')
    embed.add_field(name='Region del Server', value=f'{ctx.guild.region}')
    embed.add_field(name='Id del Server', value=f'{ctx.guild.id}')
    embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall( r"watch\?v=(\S{11})", html_content.read().decode())
    print(search_results)
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[3])

""" Events """
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name='Viendo el Canal de Drackord!', url='https://www.twitch.tv/drackord'))
    print('Estoy listo!')

bot.run(os.environ['token'])