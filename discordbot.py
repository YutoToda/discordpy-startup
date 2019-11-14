import discord
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def set_members(ctx):  
    for member in ctx.guild.members:  
        role = discord.utils.find(lambda r: r.name == '一般提督', ctx.guild.roles)  
        await member.add_roles(role)  

bot.run(token)
