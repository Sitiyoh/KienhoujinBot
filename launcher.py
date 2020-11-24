from discord.ext import commands
import os

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("on_ready")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "Bot" in message.content:
        await message.channel.send("はーい、Botでーす")

bot.run(os.environ['KienhoujinToken'])
