from nonebot.plugin.on import on_command
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import (
    Bot,
    Event,
    Message,
    GroupMessageEvent,
    GROUP_ADMIN,
    GROUP_OWNER
    )
from nonebot.permission import SUPERUSER

from nonebot.matcher import Matcher
from nonebot.params import CommandArg, Arg, RawCommand

from nonebot import logger

import asyncio
import time
import random

try:
    import ujson as json
except ModuleNotFoundError:
    import json

from pathlib import Path
path=r""

def get_message_at(data: str) -> list:
    '''
    获取at对象
    '''
    qq_list = []
    data = json.loads(data)
    try:
        for msg in data['message']:
                
            if msg['type'] == 'at':
                if int(msg['data']['qq']) not in qq_list:
                    qq_list.append(int(msg['data']['qq']))
        return qq_list
    except Exception:
        return []

add_namelist = on_command("登记", priority = 20)

@add_namelist.handle()
async def _(bot:Bot, event: GroupMessageEvent):
    user=str(event.user_id)
    with open(path, 'r', encoding="utf8") as f:
        content = json.load(f)
    if str(user) in content:
        await add_namelist.finish("已登记")
    else:
        content[user]={}
        ablity=content[user]
        ablity['攻击']=random.randint(0,5)
        ablity['防御']=random.randint(0,5)
        with open(path, "w", encoding="utf8") as b:
            json.dump(content, b, ensure_ascii=False, indent=2)
        await add_namelist.finish("登记成功,目前随机生成攻击："+str(ablity['攻击'])+"，防御"+str(ablity['防御'])+"。")

shot2 = on_command("乱杀" ,priority = 4, block=True)

@shot2.handle()
async def _(bot:Bot, event: GroupMessageEvent):
    a={}
    meml=""
    member_list = await bot.get_group_member_list(group_id = event.group_id, no_cache = True)
    at=get_message_at(event.json())
    for mem in member_list:
         a[mem['user_id']]=mem['nickname']
    for mem in at:
         meml=meml+a[mem]+"、"
    meml=meml[0:-1]
    at.append(event.user_id)
    lucky=random.randint(0,len(at)-1)
    time=random.randint(10,100)*60
    msg3=[
            "欸~~~~~~~~怎么没人出事呢，真无趣",
            "我说，你们大人就这种程度吗?wwwwww",
            "没想到这些大人都是杂鱼呢..",
            ]
    if time==0:
         await shot.finish(a[event.user_id]+"试图攻击"+meml+"，但是无事发生，"+random.choice(msg3))
    msg1=[
            f"{a[at[lucky]]}真是杂♥鱼呢",
            "好弱好弱♥",
            f"像杂鱼一样躺在地上挣扎着呢~{a[at[lucky]]}",
            f"垃圾杂鱼攻击性这么强的{a[at[lucky]]}现在看起来真可怜呢wwwww",
            f"果然{a[at[lucky]]}这种死肥宅是真的逊♥",
            f"杂鱼{a[at[lucky]]}",
            f"生气了吗♥小杂鱼{a[at[lucky]]}，记得以后降低点攻击性哦♥",
            f"{a[at[lucky]]}这种实力，蟑螂都打不过吧♥"
            ]
    msg2=[
            f"{(1/len(at))*100}%概率都会死的人，{a[at[lucky]]}出门都会被蟑螂创吧♥wwwww",
            "嘻嘻，这就是废物死宅家里蹲吗♥，真弱wwww",
            f"{a[at[lucky]]}这种杂鱼捉弄起来真无趣♥",
            f"{a[at[lucky]]}真好捉弄啊~嘻嘻♥",
            f"果然{a[at[lucky]]}这种死宅是真的逊呢♥",
            f"要不要拉报警器帮你把{a[event.user_id]}抓了呀wwwww{a[at[lucky]]}这没用的小鬼",
            f"欸~~~~这就死了吗？？{a[at[lucky]]}真的好逊哦wwwwww",
            f"嘻嘻，{a[at[lucky]]}这种大人真的不太行呢~~",
            f"死了哦♥，杂鱼{a[at[lucky]]}"
            ]
    try:
        await bot.set_group_ban(group_id = event.group_id, user_id = at[lucky], duration = time)
    except:
        pass
    if (a[at[lucky]]==a[event.user_id]):
        await shot.finish(a[event.user_id]+"试图攻击"+meml+",但是被反杀了，"+random.choice(msg1))
    await shot.finish(a[event.user_id]+"试图攻击"+meml+",最后是"+a[at[lucky]]+"死掉了喵,"+random.choice(msg2))

shot = on_command("击杀" ,priority =-1, block=False)

@shot.handle()
async def _(bot:Bot, event: GroupMessageEvent):
    a={}
    meml=""
    member_list = await bot.get_group_member_list(group_id = event.group_id, no_cache = True)
    at=get_message_at(event.json())
    for mem in member_list:
         a[mem['user_id']]=mem['nickname']
    for mem in at:
         meml=meml+a[mem]+"、"
    meml=meml[0:-1]
    at.append(event.user_id)
    lucky=random.randint(0,len(at)-1)
    time=random.randint(0,3)*60
    msg3=[
            "欸~~~~~~~~真无趣",
            "我说，你们大人就这种程度吗wwwwww",
            "没想到这些大人都是杂鱼呢~♥",
            ]
    if time==0:
         await shot.finish(a[event.user_id]+"试图攻击"+meml+"，但是什么都没发生哦？"+random.choice(msg3))
    msg1=[
            f"{a[at[lucky]]}真是杂♥鱼呢",
            "真的好弱好弱啊www♥",
            f"像杂鱼一样躺在地上挣扎着呢~www{a[at[lucky]]}",
            f"攻击性这么强的{a[at[lucky]]}现在看起来真可怜呢wwwww",
            f"果然{a[at[lucky]]}这种死肥宅是真的逊♥",
            f"真是条不可回收的杂鱼呢，{a[at[lucky]]}",
            f"小~杂~鱼~生气了吗♥？{a[at[lucky]]}记得以后降低点攻击性哦♥",
            f"{a[at[lucky]]}这种实力，蟑螂都打不过吧♥",
            f"要不要等长大点再干这种事呢？小鬼{a[at[lucky]]}ww",
            ]
    msg2=[
            f"{(1/len(at))*100}%的概率死掉了哦？不觉得挺丢人的吗ww",
            "嘻嘻，这就是废物死宅家里蹲吗♥，真弱wwww",
            f"{a[at[lucky]]}这种杂鱼捉弄起来真无趣♥",
            f"{a[at[lucky]]}真好捉弄啊~嘻嘻♥",
            f"果然{a[at[lucky]]}这种死宅是真的逊呢♥",
            f"要不要拉报警器帮你把{a[event.user_id]}抓了呀wwwww{a[at[lucky]]}这没用的小鬼",
            f"这就死了吗？？欸~~~~{a[at[lucky]]}真的好逊哦wwwwww",
            f"嘻嘻，{a[at[lucky]]}这种大人真的不太行呢~~",
            f"死了哦♥，杂鱼{a[at[lucky]]}",
            f"笨蛋{a[at[lucky]]}还能说话吗www",
            f"说话！{a[at[lucky]]}说话！",
            ]
    try:
        await bot.set_group_ban(group_id = event.group_id, user_id = at[lucky], duration = time)
    except:
        pass
    if (a[at[lucky]]==a[event.user_id]):
        await shot.finish(a[event.user_id]+"试图攻击"+meml+",但是因为太菜没能攻击成功，"+random.choice(msg1))
    await shot.finish(a[event.user_id]+"试图攻击"+meml+",最后是"+a[at[lucky]]+"死掉了,"+random.choice(msg2))
