from discord.ext import commands
import os

bot = commands.Bot(command_prefix="!")
patterns = ["機炎方陣", "破壊", "ブラフマントライデント", "シヴァ槍"]

@bot.event
async def on_ready():
    print("on_ready")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    for p in patterns:
        if p in message.content:
            await message.channel.send("機炎方陣・破壊!?")
            break

bot.run(os.environ['KienhoujinToken'])
