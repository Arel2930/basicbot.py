import discord
# Discord botları için komut tabanlı bir framework sağlar. 
# Bu framework sayesinde, botumuzun belirli komutlara yanıt vermesini kolayca tanımlayabiliriz.
from discord.ext import commands
from bot_mantik import gen_pass
import time
import random

intents = discord.Intents.default()
intents.message_content = True # botun mesaj içeriğine erişimini aktif hale getiriyoruz.

bot = commands.Bot(command_prefix='$', intents=intents)
#Bu özellik, botun kendisine gönderilen komutları tanıması için bir ön ek tanımlar.
#  $ işareti komut ön eki olarak belirlenmiştir. Yani bot sadece $ ile başlayan komutlara yanıt verir.

@bot.event # bot belirli bir olay gerçekleştiğinde tetiklensin.
async def on_ready(): # bot başarılı bir şekilde Discord'a bağlandığında tetiklenir
    print(f'{bot.user} olarak giriş yaptık')

@bot.command() # botun bir komutu tanıması için bu dekoratörü kullanırız.
async def hello(ctx): # hello adında bir komut tanımladık. ctx(context), komutun çağrıldığı yer hakkındaki bilgileri içerir.
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')
#Bu komutun çalışması için, kullanıcı sohbette $hello yazmalıdır. 

@bot.command() # botun bir komutu tanıması için bu dekoratörü kullanırız.
async def pasw(ctx): # pasw adında bir komut tanımladık. ctx(context), komutun çağrıldığı yer hakkındaki bilgileri içer
    await ctx.send(gen_pass(10))
#Bu komutun çalışması için kullanıcı $pasw yazmalıdır.

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def yazıtura(ctx):
    soru = await ctx.send(f"Yazımı turamı?")
    def Cevap(mesaj):
        return mesaj.author == ctx.author and mesaj.channel == ctx.channel
    cevap_mesajı = await bot.wait_for("message", check = Cevap)
    cevap = cevap_mesajı.content.lower()
    secim = random.randint(1,2)
    if cevap == "$yazı" or cevap == "$tura":
        await ctx.send(f"Parayı atıyorum.")
        time.sleep(3)
        await ctx.send(f"Attım.")
        time.sleep(1)
    if secim == 1:
        if cevap == "$yazı":
            await ctx.send(f"Doğru bildin.")
        elif cevap == "$tura":
            await ctx.send(f"Yanlış bildin.")
        else:
            if cevap.strip():
                await ctx.send(f"Böyle bir seçenek yok.")
    elif secim == 2:
        if cevap == "$yazı" or cevap == "$tura":
            with open("Resimler/Resim5.png","rb") as f:
                picture = discord.File(f)
            await ctx.send(file = picture)
        if cevap == "$yazı":
            await ctx.send(f"Yanlış bildin.")
        elif cevap == "$tura":
            await ctx.send(f"Doğru bildin.")
        else:
            if cevap.strip():
                await ctx.send(f"Böyle bir seçenek yok.")
#not working
@bot.command()
async def ucaklarnapar(ctx):
    await ctx.send(f"Uçaklar tabii ki uçar, fuww fouw")

@bot.command()
async def geri_donusum(ctx):
    soru1 = await ctx.send(f"hangi tür(1. yeniden kullanılabilir malzemeler/ 2. yeniden kullanılarbilir malzemelerle ne yapabiliriz)?")
    def Cevap(mesaj):
        return mesaj.author == ctx.author and mesaj.channel == ctx.channel
    cevap_mesajı = await bot.wait_for("message", check = Cevap)
    cevap = cevap_mesajı.content.lower()
    if cevap == "$1" or cevap == "$2":
        if cevap == "$1":
            await ctx.send("Platik, Kağıt, Metal, Cam ve Odun malzemeleri geri dönüştürülebilir")
    elif cevap == "$2":
        await ctx.send("Mesela platik bir şişeyle bi kalemlik veya saksı yapabilirsin.")
    
bot.run("token")
