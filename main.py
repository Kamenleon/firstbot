#ver1.05
import discord
import urllib.request
import json
import re
import random
import datetime
#import gspread

client = discord.Client()

def skill(msg2):
    cardlist = []
    if "ユリナ（第一章）" in msg2:
        card = ["【乱打】","【癇癪玉】","【不完全浦浪嵐】"]
        cardlist.extend(card)
    elif "ユリナ" in msg2:
        card = ["【気炎万丈】","【居合】","【浦浪嵐】"]
        cardlist.extend(card)
    if "サイネ（第2章）" in msg2:
        card = ["【氷の音】","【伴奏】","【二重奏:弾奏氷明】"]
        cardlist.extend(card)
    elif "サイネ（徒神）" in msg2:
        card = ["【裏斬り】","【遺響壁】","【絶唱絶華】"]
        cardlist.extend(card)
    elif "サイネ" in msg2:
        card = ["【見切り】","【石突】","【響鳴共振】"]
        cardlist.extend(card)
    if "トコヨ（旅芸人）" in msg2:
        card = ["【陽の音】","【奏流し】","【二重奏:吹弾陽明】"]
        cardlist.extend(card)
    elif "トコヨ" in msg2:
        card = ["【風舞台】","【要返し】","【常世の月】"]
        cardlist.extend(card)
    if "ヒミカ（原初）" in msg2:
        card = ["【火炎流】","【殺意】","【炎天・紅緋弥香】"]
        cardlist.extend(card)
    elif "ヒミカ" in msg2:
        card = ["【フルバースト】","【スモーク】","【クリムゾンゼロ】"]
        cardlist.extend(card)
    if "オボロ（第3章）" in msg2:
        card = ["【手裏剣】","【不意打ち】","【神代枝】"]
        cardlist.extend(card)
    elif "オボロ" in msg2:
        card = ["【分身の術】","【生体活性】","【虚魚】","【鳶影】"]
        cardlist.extend(card)
    if "ユキヒ" in msg2:
        card = ["【しこみばり/ふくみばり】","【かさまわし】","【どろりうら】"]
        cardlist.extend(card)
    if "シンラ（教主）" in msg2:
        card = ["【真言】","【使徒】","【全知経典】"]
        cardlist.extend(card)
    elif "シンラ" in msg2:
        card = ["【立論】","【森羅判証】","【皆式理解】","【天地反駁】"]
        cardlist.extend(card)
    if "ハガネ" in msg2:
        card = ["【大地砕き】","【引力場】","【大天空クラッシュ】"]
        cardlist.extend(card)
    if "チカゲ（第4章）" in msg2:
        card = ["【仕掛け番傘】","【奮迅】","【残滓の絆毒】"]
        cardlist.extend(card)
    elif "チカゲ" in msg2:
        card = ["【首切り】","【飛苦無】","【闇昏千影の生きる道】"]
        cardlist.extend(card)
    if "クルル（探検家）" in msg2:
        card = ["【あならいず】","【だうじんぐ】","【らすとりさーち】"]
        cardlist.extend(card)
    elif "クルル" in msg2:
        card = ["【りげいなー】","【えれきてる】","【いんだすとりあ】"]
        cardlist.extend(card)
    if "サリヤ" in msg2:
        card = ["【Shield Charge】","【Steam Cannon】","【Julia`s Blackbox】"]
        cardlist.extend(card)
    if "ライラ" in msg2:
        card = ["【雷爆風神爪】","【天雷召喚陣】","【円環輪廻旋】"]
        cardlist.extend(card)
    if "ホノカ" in msg2:
        card = ["【義旗共振】","【桜の翅】","【胸に想いを】"]
        cardlist.extend(card)
    if "ウツロ（終章）" in msg2:
        card = ["【蝕みの塵】","【残響装置:枢式】","【虚偽】"]
        cardlist.extend(card)
    elif "ウツロ" in msg2:
        card = ["【影の翅】","【遺灰呪】","【灰滅】"]
        cardlist.extend(card)
    if "コルヌ" in msg2:
        card = ["【凍縛場】","【絶対零度】","【ポルチャルトー】"]
        cardlist.extend(card)
    if "ヤツハ" in msg2:
        card = ["【昏い顎】","【寄花】","【六葉鏡の星の海】"]
        cardlist.extend(card)
    return cardlist

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
            msge = "猫じゃないんですよ！"
        elif message.content.startswith("!更新情報"):#ver1.05
            msge = "既存のコマンドの改良を行いました！"
        elif message.content == "!wiki":
            msge =  "身内用TRPGのwikiです。管理人のやる気がないとか言わないでくださいね\nhttps://seesaawiki.jp/trpgon0924/"
        elif message.content == "!invite":
            if message.channel.id == 561494317940604957: 
                msge = "ようこそ千本桜チャンネルへ！\nここのサポートキャラクター、ホノカと申します！\n分からないことあれば【!help】コマンドからコマンドを確認して下さい\nそれでは、桜降る代に決闘を！"
            elif message.channel.id == 423298530837397505:
                msge = "あーマイクのテスト中\nこのチャンネルの説明は必要ありませんよね？"
            elif message.channel.id == 309050914231156736:
                msge = "ようこそ、General Serverに！\nこちらではTRPGをプレイする際の募集、長期休暇に行われるゲーム会の日程調整などが行われます\n本サーバーのマスコットキャラクター、ホノカと申します！\n分からないことあれば【!help】とコマンドを打ってください。私とDMでも結構です。\n"
            else:
                msge = "ここのチャンネルは説明不要かと！"
        elif message.content.startswith("!help"):
            msge = "①こちらが私のコマンドリストです！\n通常用  【!wiki】,【!invite】,【!neko】,【@Honoka】,【!fortune】,【天気○○(地域限定)】\n桜降る代に決闘を用  【!board】,【!pair】,【!pair2】（第三拡張非対応バージョン）,【!turn】,【megami〇（数字）】,【!rabo】\n\n②また、いくつかの言葉に反応します！\n\n"
            dm = await message.author.create_dm()
            await dm.send(msg + "お役に立ちましたでしょうか？")
            return
        elif message.content == "!pair":
            mylist = ["【ユリナ】","【ユリナ（第1章）】","【サイネ（第2章）】","【サイネ】","【トコヨ】","【トコヨ（旅芸人）】","【ヒミカ】","【ヒミカ（原初）】","【オボロ】","【オボロ（第3章）】","【ユキヒ】","【シンラ】","【ハガネ】","【チカゲ】","【チカゲ（第4章）】","【クルル】","【サリヤ】","【ライラ】","【ホノカ】","【ウツロ】","【ウツロ（終章）】","【ヤツハ】","【コルヌ】","【シンラ（教主）】","【クルル（探索者）】","【サイネ（徒神）】"]
            s = ','
            msg2 = s.join(random.sample(mylist,2)) 
            msge = u'{},{}'.format(message.author.mention,msg2)
            point = ["を使われてはいかがでしょうか？","を使ってみましょう！","はお勧めですよ！","もありかもです！","の組み合わせが見てみたいです！"]
            if message.user.id != 235269796235706368:
                msge = msge + random.choice(point)
                await message channel.send()
                return 
            splitset = msg2.split(",")
            cardset1 = skill(splitset[0])
            cardset2 = skill(splitset[1])
            best2 = random.choice(cardset1) + "," + random.choice(cardset2) + random.choice(point)
            msge = msge + "\n" + best2
        elif message.content == "!pair2":
            mylist = ["【ユリナ】","【ユリナ（第1章）】","【サイネ（第2章）】","【サイネ】","【トコヨ】","【トコヨ（旅芸人）】","【ヒミカ】","【ヒミカ（原初）】","【オボロ】","【オボロ（第3章）】","【ユキヒ】","【シンラ】","【ハガネ】","【チカゲ】","【チカゲ（第4章）】","【クルル】","【サリヤ】","【ライラ】","【ホノカ】","【ウツロ】","【ウツロ（終章）】"]
            s = ','
            msg2 = s.join(random.sample(mylist,2)) 
            msge = u'{},{}'.format(message.author.mention,msg2)
        elif message.content.startswith("!turn"):
            mylist1 =["プレイヤー①","プレイヤー②"]
            mylist2 = ["様の先制攻撃です！","様が先攻です！","様が先に勝負を仕掛けました！","様が先手です"]
            mylist3 = ["【野生の】","【紅蓮の】","【歴戦の】","【狂気の】","","","【武神の】","【舞姫の】","【塵滅の】","【風来の】","【衝撃の】","【楽師の】","","【叡智の】","","【絡繰の】","【氷結の】","【探索者の】","【鏡映の】","【徒神の】","【教主の】","【終章の】"]
            msge = random.choice(mylist3) + random.choice(mylist1) + random.choice(mylist2)
        elif message.content.startswith("!board"):
            msge = "胸に想いを 両手に花を 桜降る代に決闘を!\nプレイヤー1の参加用URL	https://furuyoni-simulator.herokuapp.com/play/VZwiZUphVNMn\nプレイヤー2の参加用URL	https://furuyoni-simulator.herokuapp.com/play/NDXtvn7rUdNt\n観戦用URL	https://furuyoni-simulator.herokuapp.com/watch/6471"
        elif message.content.startswith("megami"):
            content = message.content
            pattern = '.*?(\d+).*'
            result = re.match(pattern,content)
            if result:
                number = int(result.group(1))
                if(number > 16):
                    print("メガミは16人までしかおりません！,16までの数字でお願いします！")
                    return
                mylist = ["【ユリナ】","【サイネ】","【トコヨ】","【ヒミカ】","【オボロ】","【ユキヒ】","【シンラ】","【ハガネ】","【チカゲ】","【クルル】","【サリヤ】","【ライラ】","【ホノカ】","【ウツロ】","【コルヌ】","【ヤツハ】"]
                s = ','
                msge = s.join(random.sample(mylist,number))
        elif message.content == "!fortune": # Embedを使ったメッセージ送信 と ランダムで要素を選択
            msg1 = "http://bakafire.main.jp/twi_icon/twiicon_sa_"
            mylist1 = ["01","02","03","04","05a","05b","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"]
            jpg = ".jpg"
            icon = msg1 + random.choice(mylist1)+jpg
            embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢は！",color=0x2ECC69)
            embed.set_thumbnail(url=icon)
            if(icon == "http://bakafire.main.jp/twi_icon/twiicon_sa_13.jpg"):
                embed.add_field(name="[運勢] ", value="満天", inline=False)
                embed.add_field(name="[女神から]", value='おめでとうございます、今日は最高の日ですよ！', inline=False)
            elif(icon == "http://bakafire.main.jp/twi_icon/twiicon_sa_10.jpg"):
                embed.add_field(name="[運勢] ", value="たのしーひ", inline=False)
                embed.add_field(name="[女神から]", value='わたしといっしょにじっけんしましょー', inline=False)
            elif(icon == "http://bakafire.main.jp/twi_icon/twiicon_sa_25.jpg"):

                embed.add_field(name="[運勢] ", value="れっつごー！", inline=False)

                embed.add_field(name="[女神から]", value='振り返らないこともまた大切なのです！', inline=False)
            else:
                embed.add_field(name="[運勢] ", value=random.choice(('大吉','大吉','吉','吉','吉','凶','凶', '凶', '大凶')), inline=False)
            await message.channel.send(embed=embed)
            return
        elif u'{}'.format(client.user.id) in message.content: # 話しかけられたかの判定
            msge = u'{} はい、なんでしょう！'.format(message.author.mention)  # 返信文の作成
        elif message.content.startswith("こんにちは"):
            msge = "こんにちは、" + message.author.name + "さん！"
        elif message.content == "ありがとう":
            mylist = ["どういたしまして！","お役に立てて、嬉しいです！","いつでもどうぞ!","いえいえ！","もっと頼ってくださいね！"]
            msge = random.choice(mylist)
        elif message.content == '大丈夫や':
            mylist = ["本当ですか？","そうならいいのですが…"]
            msge = random.choice(mylist)
        elif message.content == "バカ":
            msge = "バカって言うほうがバカなんですよ！"
        elif message.content.startswith("だ、誰だ貴様"):
            msge = "ぽわぽわちゃんです！"
        elif message.content.startswith("眠たい"):
            mylist = ["寝ましょう","寝てください","お休みの時間ですよ","徹夜でもされたんですか？"]
            msge = random.choice(mylist)
            await message.channel.send(f"{message.author.mention}さん、" + msge)
            return
        elif message.content.startswith("!rabo"):
            msge = "くるる～ん!\nhttps://main-bakafire.ssl-lolipop.jp/furuyoni/kururun_lab/"
        elif message.content.startswith("天気"):
            reg_res = re.compile(u"天気(.+)").search(message.content)
            if reg_res:
                if reg_res.group(1) in citycodes.keys():
                    citycode = citycodes[reg_res.group(1)]
                    resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()
                    resp = json.loads(resp.decode('utf-8'))
                    
                    msge = resp['location']['city']
                    msge += "の天気は、\n"
                    for f in resp['forecasts']:
                        msge += f['dateLabel'] + "が" + f['telop'] + "\n"
                    msge += "です。  お役に立てましたか？"
                    await message.channel.send(message.author.mention + msge)
                    return
                else:
                    await message.channel.send("ごめんなさい、そこの天気は分かりません...")
        else:
            return
        await message.channel.send(msge)

client.run("")
