import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# ... كمل باقي كود الأتمتة حقك هنا ...

bot.run("MTUyMjU2MzQwNTEzMzY0Mzg4OA.GQ579_.idi8GI5YIQex5CES3HvVJS9PqqHWP5AlPNNN1g")
