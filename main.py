#ver1.03
import discord
import urllib.request
import json
import re
import random
import datetime

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

@client.event
async def on_message(message):
    if client.user != message.author:
        if message.content.startswith('!neko'):
            msg = "猫じゃないんですよ！"
        elif message.content.startswith("!更新情報"):#ver1.03
            msg = "いくつかのコマンドを追加しました。詳しくは【!help】\nまた既存のコマンドも改良しています。"
        elif message.content == "!wiki":
            msg =  "身内用TRPGのwikiです。管理人がやる気ないとか言わないでくださいね\nhttps://seesaawiki.jp/trpgon0924/"
        elif message.content == "!invite":
            if message.channel.id == 561494317940604957: 
                msg = "ようこそ千本桜チャンネルへ！\nここのサポートキャラクター、ホノカと申します！\n分からないことあれば【!help】コマンドからコマンドを確認して下さい\nそれでは、桜降る代に決闘を！"
            elif message.channel.id == 423298530837397505:
                msg = "あーマイクのテスト中\nこのチャンネルの説明は必要ありませんよね？"
            elif message.channel.id == 309050914231156736:
                msg = "ようこそ、General Serverに！\nこちらではTRPGをプレイする際の募集、長期休暇に行われるゲーム会の日程調整などが行われます\n本サーバーのマスコットキャラクター、ホノカと申します！\n分からないことあれば【!help】とコマンドを打ってください。私とDMでも結構です。\n"
        elif message.content.startswith("!help"):
            msg = "①こちらが私のコマンドリストです！\n通常用  【!wiki】,【!invite】,【!neko】,【@Honoka】,【!fortune】,【天気○○(地域限定)】\n桜降る代に決闘を用  【!board】,【!pair】,【!turn】,【megami〇（数字）】,【!rabo】\n\n②また、いくつかの言葉に反応します！\n\n"
            dm = await message.author.create_dm()
            await dm.send(msg + "お役に立ちましたでしょうか？")
            return
        elif message.content.startswith("!pair"):
            mylist = ["【ユリナ】","【ユリナ（第1章）】","【サイネ（第2章）】","【サイネ】","【トコヨ】","【トコヨ（旅芸人）】","【ヒミカ】","【ヒミカ（原初）】","【オボロ】","【オボロ（第3章）】","【ユキヒ】","【シンラ】","【ハガネ】","【チカゲ】","【チカゲ（第4章）】","【クルル】","【サリヤ】","【ライラ】","【ホノカ】","【ウツロ】","【ウツロ（終章）】"]
            s = ','
            msg2 = s.join(random.sample(mylist,2)) 
            msg = u'{},{}'.format(message.author.mention,msg2)
        elif u'{}'.format(client.user.id) in message.content: # 話しかけられたかの判定
            msg = u'{} はい、なんでしょう！'.format(message.author.mention)  # 返信文の作成
        elif message.content.startswith("こんにちは"):
            msg = "こんにちは、" + message.author.name + "さん！"
        elif message.content.startswith("ありがとう"):
            mylist = ["どういたしまして！","お役に立てて、嬉しいです！","いつでもどうぞ!","いえいえ！","もっと頼ってくださいね！"]
            msg = random.choice(mylist)
        elif message.content.startswith("!turn"):
            mylist1 =["プレイヤー①","プレイヤー②"]
            mylist2 = ["様の先制攻撃です！","様が先攻です！","様が先に勝負を仕掛けました！","様が先手です"]
            mylist3 = ["【野生の】","【紅蓮の】","【歴戦の】","【狂気の】","","","","","【八面六臂の】","【武神の】","【舞姫の】","【塵滅の】","【風来の】","【衝撃の】","【楽師の】","","【叡智の】","","【絡繰の】","【氷結の】","【探索者の】","【鏡映の】"]
            msg = random.choice(mylist3) + random.choice(mylist1) + random.choice(mylist2)
       　elif message.content.startswith("!board"):
            msg = "胸に想いを 両手に花を 桜降る代に決闘を!\nプレイヤー1の参加用URL	https://furuyoni-simulator.herokuapp.com/play/VZwiZUphVNMn\nプレイヤー2の参加用URL	https://furuyoni-simulator.herokuapp.com/play/NDXtvn7rUdNt\n観戦用URL	https://furuyoni-simulator.herokuapp.com/watch/6471"
        elif message.content == '大丈夫や':
            mylist = ["本当ですか？","そうならいいのですが…"]
            msg = random.choice(mylist)
        elif message.content.startswith("megami"):
            content = message.content
            pattern = '.*?(\d+).*'
            result = re.match(pattern,content)
            if result:
                number = int(result.group(1))
                mylist = ["ユリナ ","サイネ ","トコヨ ","ヒミカ ","オボロ ","ユキヒ ","シンラ ","ハガネ ","チカゲ ","クルル ","サリヤ ","ライラ ","ホノカ ","ウツロ "]
                s = ','
                msg = s.join(random.sample(mylist,number))
        elif message.content == "!fortune": # Embedを使ったメッセージ送信 と ランダムで要素を選択
            embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢は！",color=0x2ECC69)
            embed.set_thumbnail(url=message.author.avatar_url)
            embed.add_field(name="[運勢] ", value=random.choice(('大吉','大吉','吉','吉','吉','凶','凶', '凶', '大凶')), inline=False)
            await message.channel.send(embed=embed)
            return
        elif message.content.startswith("バカ"):
            msg = "バカって言うほうがバカなんですよ！"
        elif message.content.startswith("だ、誰だ貴様"):
            msg = "ぽわぽわちゃんです！"
        elif message.content.startswith("眠たい"):
            mylist = ["寝ましょう","寝てください","お休みの時間ですよ","徹夜されたんですか？"]
            msg = random.choice(mylist)
            await message.channel.send(f"{message.author.mention}さん、" + msg)
            return
        elif message.content.startswith("!rabo"):
            msg = "くるる～ん!\nhttps://main-bakafire.ssl-lolipop.jp/furuyoni/kururun_lab/"
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
                    return
                else:
                    await message.channel.send("ごめんなさい、そこの天気は分かりません...")
        else:
            return
        await message.channel.send(msg)

@client.event
async def on_member_join(self, member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = '{0.mention}さん、 {1.name}へようこそ!\n楽しくやっていきましょうね'.format(member, guild)
        await guild.system_channel.send(to_send)

client.run("NTY1MTE1NDY1MTIzMjMzODAy.XKxu5g.h4gKk10iuuMfo47oiV_aJZTQGk0")
