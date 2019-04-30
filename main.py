import discord
import urllib.request
import json
import re
import random

client = discord.Client()

citycodes = {
    "名古屋": '230010',
    "東京"   : '130010',
    "大阪"   : '270000',
    "京都"   : '260010',
    "福井"   : '180010',
    "岡山"   : '330010',
    "大津"   : '250010',
    "彦根"   : '250020',
    "広島"   : '340010',
    "福岡"   : '400010',
    "鹿児島": '460010',
    "那覇"   : '471010'
}

@client.event
async def on_ready():
    print("logged in as " + client.user.name)
    channel = client.get_channel('564818590935547925')

@client.event
async def on_message(message):
    if client.user != message.author:
        if message.content.startswith('!neko'):
            reply = "猫じゃないんですよ！"
            await message.channel.send(reply)
        elif message.content.startswith("!更新情報"):
            msg = "【!pair】で被ることがなくなりました,やりましたね！\n【!fortune】でおみくじができます。大凶が出てもへこまないでくださいね"
            await message.channel.send(msg)
        elif message.content.startswith("!help"):
            msg = "こちらが私のコマンドリストです！\n【!neko】,【!board】,【!pair】,【!turn】,【@Honoka】,【!fortune】,\n【megami〇（数字の数、女神をランダムに選出します）】,【天気○○(地域限定)】\nまた、いくつかの言葉に反応します！"
            await message.channel.send(msg)
        elif u'{}'.format(client.user.id) in message.content: # 話しかけられたかの判定
            msg = u'{} はい、なんでしょう！'.format(message.author.mention)  # 返信文の作成
            await message.channel.send(msg)
        elif message.content.startswith("こんにちは"):
            msg = "こんにちは、" + message.author.name + "さん！"
            await message.channel.send(msg)
        elif message.content.startswith("ありがとう"):
            mylist = ["どういたしまして！","お役に立てて、嬉しいです！","いつでもどうぞ!","いえいえ！","もっと頼ってくださいね！"]
            reply = random.choice(mylist)
            await message.channel.send(reply)
        elif message.content.startswith("!turn"):
            mylist1 =["プレイヤー①","プレイヤー②"]
            mylist2 = ["様の先制攻撃です！","様が先攻です！","様が先に勝負を仕掛けました！","様が先手です"]
            mylist3 = ["【野生の】","【紅蓮の】","【歴戦の】","【狂気の】","","","","","【修羅偏在の】","【八面六臂の】","【武神の】","【舞姫の】","【塵滅の】","【風来の】","","【衝撃の】","【楽師の】","","【叡智の】","","【絡繰の】"]
            msg = random.choice(mylist3) + random.choice(mylist1) + random.choice(mylist2)
            await message.channel.send(msg)
        elif message.content.startswith("!board"):
            reply = "胸に想いを 両手に花を 桜降る代に決闘を!\nプレイヤー1の参加用URL: https://furuyoni-simulator.herokuapp.com/play/FW6pXbHUQFqv\nプレイヤー2の参加用URL: https://furuyoni-simulator.herokuapp.com/play/5QkC4KQCHPGc\n観戦用URL: https://furuyoni-simulator.herokuapp.com/watch/4867"
            await message.channel.send(reply)
        elif message.content.startswith("!pair"):
            mylist = ["【ユリナ】","【ユリナ（第1章）】","【サイネ（第2章）】","【サイネ】","【トコヨ】","【トコヨ（旅芸人）】","【ヒミカ】","【ヒミカ（原初）】","【オボロ】","【オボロ（第3章）】","【ユキヒ】","【シンラ】","【ハガネ】","【チカゲ】","【チカゲ（第4章）】","【クルル】","【サリヤ】","【ライラ】","【ホノカ】","【ウツロ】","【ウツロ（終章）】"]
            s = ','
            msg = s.join(random.sample(mylist,2)) 
            await message.channel.send(msg)
        elif message.content.startswith("megami"):
            content = message.content
            pattern = '.*?(\d+).*'
            result = re.match(pattern,content)
            if result:
                number = int(result.group(1))
                mylist = ["ユリナ ","サイネ ","トコヨ ","ヒミカ ","オボロ ","ユキヒ ","シンラ ","ハガネ ","チカゲ ","クルル ","サリヤ ","ライラ ","ホノカ ","ウツロ "]
                s = ','
                mystr = s.join(random.sample(mylist,number))
                await message.channel.send(mystr)
        elif message.content == "!fortune": # Embedを使ったメッセージ送信 と ランダムで要素を選択
            embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢は！",color=0x2ECC69)
            embed.set_thumbnail(url=message.author.avatar_url)
            embed.add_field(name="[運勢] ", value=random.choice(('大吉','大吉','吉','吉','吉','凶','凶', '凶', '大凶')), inline=False)
            await message.channel.send(embed=embed)
        elif message.content.startswith("バカ"):
            reply = "バカって言うほうがバカなんですよ！"
            await message.channel.send(reply)
        elif message.content.startswith("だ、誰だ貴様"):
            reply = "ぽわぽわちゃんです！"
            await message.channel.send(reply) 
        elif message.content.startswith("眠たい"):
            mylist = ["寝ましょう","寝てください","お休みの時間ですよ","徹夜されたんですか？"]
            reply = random.choice(mylist)
            await message.channel.send(f"{message.author.mention}さん、" + reply)
        elif message.content.startswith("天気"):
            reg_res = re.compile(u"天気(.+)").search(message.content)
            if reg_res:
                if reg_res.group(1) in citycodes.keys():
                    citycode = citycodes[reg_res.group(1)]
                    resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()
                    resp = json.loads(resp.decode('utf-8'))
                    
                    msg = resp['location']['city']
                    msg += "の天気は、\n"
                    for f in resp['forecasts']:
                        msg += f['dateLabel'] + "が" + f['telop'] + "\n"
                    msg += "です。  お役に立てましたか？"
                    await message.channel.send(message.author.mention + msg)
                else:
                    await message.channel.send("ごめんなさい、そこの天気は分かりません...")

client.run("NTY1MTE1NDY1MTIzMjMzODAy.XKxu5g.h4gKk10iuuMfo47oiV_aJZTQGk0")
