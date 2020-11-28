from discord.ext import commands
from reply import Reply
import discord
import os

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("on_ready")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    reaction = Reply.React(message.content)

    if type(reaction) is str:
        await message.channel.send(reaction)
    elif type(reaction) is not None:
        await message.channel.send(file=reaction.File())

bot.run(os.environ['KienhoujinToken'])
