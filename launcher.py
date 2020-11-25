from discord.ext import commands
import discord
import os
import random

bot = commands.Bot(command_prefix="!")
patterns1 = ["機炎方陣", "破壊", "機炎方陣・破壊", "機炎方陣破壊"]
patterns2 = ["ブラフマントライデント", "シヴァ槍"]

@bot.event
async def on_ready():
    print("on_ready")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if patterns1[2] in message.content or patterns1[3] in message.content:
        await send_message(message, patterns1[2] + "！？")
    elif patterns1[0] in message.content:
        await send_message(message, patterns1[1] + "！？")
    elif patterns1[1] in message.content:
        await send_message(message, patterns1[0] + "！？")
    else:
        for p in patterns2:
            if p in message.content:
                rnd = random.randint(1, 2)
                await send_picture(message, f"image/BrahmanTrident{rnd}.png")

async def send_message(message, text):
    await message.channel.send(text)

async def send_picture(message, picture_path):
    await message.channel.send(file=discord.File(picture_path))

bot.run(os.environ['KienhoujinToken'])
