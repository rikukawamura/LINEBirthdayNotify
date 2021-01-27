from line_notify_bot import LINENotifyBot
import datetime

# coding: UTF-8
date = str(datetime.date.today()).split('-')
month, day = date[1], date[2]

bot = LINENotifyBot(access_token='アクセストークンをペースト')

if month=='月(e.g.01)' and day=='日(e.g.01)':
    bot.send(
        message='\n{}月{}日は{}の誕生日'.format(month, day, '名前')
    )
elif month=='01' and day=='01':
    bot.send(
        message='\n{}月{}日は{}の誕生日'.format(month, day, '山田太郎')
    )
