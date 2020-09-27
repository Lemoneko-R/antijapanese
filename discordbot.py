import discord #Imports==
import unicodedata #==

#Set client
client = discord.Client()

#function
def is_japanese(string):
    for ch in string: #loop strings
        name = unicodedata.name(ch) #Str to Uni
        if "CJK UNIFIED" in name \ #Kanji check
        or "HIRAGANA" in name \ #Hiragana check
        or "KATAKANA" in name: #Katakana check
            return True #If include
    return False #Not include
# 起動時に通知してくれる処理
@client.event
async def on_ready():
    print('ログインしました')

#Discord Message recieve event
@client.event
async def on_message(message):
    if client.user != message.author:
        if message.channel.id == "550280477295247362": #Set channel ID
            if is_japanese(message.content):
                reply = f"{message.author.mention} ```Hey you! This message contains JAPANESE!! TakeCare.. \n おいお前! このメッセージには日本語が含まれてるぞ!! 気をつけろよ!!```" # 返信文の作成
                await client.send_message(message.channel, reply)    
        
    if client.user.id in message.content: # 話しかけられたかの判定
        reply = 'Hello, how u doing?'# 返信文の作成
        await client.send_message(message.channel, reply) 
# botの接続と起動
# （tokenにはbotアカウントのアクセストークンを入れてください）
client.run('TOKEN HERE')
