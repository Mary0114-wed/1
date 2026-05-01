import discord
from discord.ext import commands, tasks
import requests
from bs4 import BeautifulSoup
from flask import Flask
from threading import Thread
import os

TOKEN = os.environ.get("TOKEN")  # 🔥 여기 중요 (토큰 숨김)
CHANNEL_ID = 1488515807892738151
SOOP_URL = "https://www.sooplive.com/station/kkcy2445"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

was_live = False

🔥 서버 안 꺼지게 하는 코드

app = Flask('')

@app.route('/')
def home():
return "alive"

def run():
app.run(host='0.0.0.0', port=8080)

def keep_alive():
t = Thread(target=run)
t.start()

def is_live():
try:
headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get(SOOP_URL, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")
return "방송중" in soup.get_text()
except:
return False

@bot.event
async def on_ready():
print(f"{bot.user} 로그인 완료!")
check_stream.start()

@tasks.loop(seconds=60)
async def check_stream():
global was_live
channel = bot.get_channel(CHANNEL_ID)

if channel is None:  
    print("채널 못 찾음")  
    return  

live = is_live()  

if live and not was_live:  
    embed = discord.Embed(  
        title="🔥 용님 방송 시작!",  
        description="지금 바로 시청하러 가기",  
        color=0x5865F2  
    )  
    embed.add_field(name="🔗 링크", value=SOOP_URL, inline=False)  

    await channel.send(  
        content="@everyone 🔥 용 Streaming on!",  
        embed=embed,  
        allowed_mentions=discord.AllowedMentions(everyone=True)  
    )  

was_live = live

keep_alive()
bot.run(TOKEN)