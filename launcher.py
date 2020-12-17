from discord.ext import commands
from reply import Reply
import discord
import os
import matchPic

bot = commands.Bot(command_prefix="!")
TEMP_FILE_PATH = "tmp"

@bot.event
async def on_ready():
    print("on_ready")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.attachments:
        for a in message.attachments:
            filepath = "{0}/{1}".format(TEMP_FILE_PATH, a.filename)
            await a.save(fp=filepath)
            if matchPic.JudgeMatching(filepath):
                # 雑
                message.content += "破壊"
            os.remove(filepath)

    reaction = Reply.React(message.content)

    if reaction is None:
        return

    print("{0} {1} {2}:{3} {4}".format(message.content, message.author, message.guild, message.channel, message.created_at))

    if type(reaction) is str:
        await message.channel.send(reaction)
    else:
        await message.channel.send(file=reaction.File())

bot.run(os.environ['KienhoujinToken'])
