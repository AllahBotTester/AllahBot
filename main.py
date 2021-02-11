import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix =  '~')
yGifs = ["https://media.discordapp.net/attachments/799771858504253440/804796003865198632/yogfish.gif","https://media.discordapp.net/attachments/799771858504253440/804783434399875072/Stinky.gif","https://media.discordapp.net/attachments/799771858504253440/804600063330353192/yoomed.gif","https://media.discordapp.net/attachments/799771858504253440/804596541490855946/okay_buddy.gif"]
frazita = ""

# Easter Eggs

@client.command()
async def waifu(ctx):
    await ctx.send(f"You're {random.randrange(1,101)}/100 on the waifu scale.")

@client.command()
async def gay(ctx):
    await ctx.send(f"You're {random.randrange(1,101)}/100 on the gay scale.")

@client.command()
async def meme(ctx):
      await ctx.send(f"You're {random.randrange(1,101)}/100 on the meme scale.")

# Emotes
@client.command()
async def yogfish(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(yGifs[0])

@client.command()
async def yinky(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(yGifs[1])

@client.command()
async def yoomed(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(yGifs[2])

@client.command()
async def yokaybuddy(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(yGifs[3])


# QOL

@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! {round(client.latency*1000)}ms')

@client.command()
@commands.has_role("King")
async def clear(ctx,amount=6):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_role("King")
async def mute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="No talk")
    await member.add_roles(role)

client.run("NjM0MjQzMzEyOTY2MDQxNjEw.Xafw3w.iW6N2HgBwLCHnncTqMPV9ALL7J4")