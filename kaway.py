# -*- coding: utf-8 -*- 
import TEGUH
from TEGUH import *
from akad.ttypes import *
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from multiprocessing import Pool, Process
from humanfriendly import format_timespan, format_size, format_number, format_length
from time import sleep
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse
from datetime import timedelta, date
from datetime import datetime
import html5lib,shutil
import wikipedia,goslate
import ffmpy
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl
# SC NEW UPDATE V3.5
# https://line.me/ti/p/~gerhanaselatan
# https://line.me/ti/p/~cyberline.xxxx


cl = LineClient("email"," sandi")
cl.log("Auth Token : " + str(cl.authToken))
channel = LineChannel(cl)
cl.log("Channel Access Token : " + str(channel.channelAccessToken))


ki = LineClient("email"," sandi")
ki.log("Auth Token : " + str(ki.authToken))
channel = LineChannel(ki)
ki.log("Channel Access Token : " + str(channel.channelAccessToken))

kk = LineClient("email"," sandi")
kk.log("Auth Token : " + str(kk.authToken))
channel = LineChannel(kk)
kk.log("Channel Access Token : " + str(channel.channelAccessToken))

kc = LineClient("email"," sandi")
kc.log("Auth Token : " + str(kc.authToken))
channel = LineChannel(kc)
kc.log("Channel Access Token : " + str(channel.channelAccessToken))

kb = LineClient("email"," sandi")
kb.log("Auth Token : " + str(kb.authToken))
channel = LineChannel(kb)
kb.log("Channel Access Token : " + str(channel.channelAccessToken))

kd = LineClient("email"," sandi")
kd.log("Auth Token : " + str(kd.authToken))
channel = LineChannel(kd)
kd.log("Channel Access Token : " + str(channel.channelAccessToken))

ke = LineClient("email"," sandi")
ke.log("Auth Token : " + str(ke.authToken))
channel = LineChannel(ke)
ke.log("Channel Access Token : " + str(channel.channelAccessToken))

kf = LineClient("email"," sandi")
kf.log("Auth Token : " + str(kf.authToken))
channel = LineChannel(kf)
kf.log("Channel Access Token : " + str(channel.channelAccessToken))

kj = LineClient("email"," sandi")
kj.log("Auth Token : " + str(kj.authToken))
channel = LineChannel(kj)
kj.log("Channel Access Token : " + str(channel.channelAccessToken))

sw = LineClient("email"," sandi")
sw.log("Auth Token : " + str(sw.authToken))
channel = LineChannel(sw)
sw.log("Channel Access Token : " + str(channel.channelAccessToken))
print("\nBOT MULAI MAIN BOSS......\n")

poll = LinePoll(cl)
call = cl
creator = ["uf50d888821632d32461e37153ac775c0"]
owner = ["uf50d888821632d32461e37153ac775c0"]
admin = ["uf50d888821632d32461e37153ac775c0"]
staff = ["uf50d888821632d32461e37153ac775c0"]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kb.getProfile().mid
Emid = kd.getProfile().mid
Fmid = ke.getProfile().mid
Gmid = kf.getProfile().mid
Jmid = kj.getProfile().mid
Zmid = sw.getProfile().mid
KAC = [cl,ki,kk,kc,kb,kd,ke,kf]
ABC = [cl,ki,kk,kc,kb,kd,ke,kf]
GHOST = [kj,sw]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Jmid,Zmid]
Terx = admin + staff 

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectantijs = []
protectinvite = []
protectcancel = []
ghost = []
welcome = []
left = []
msg_dict = {}
msg_dict1 = {}

responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = kb.getProfile().displayName
responsename5 = kd.getProfile().displayName
responsename6 = ke.getProfile().displayName
responsename7 = kf.getProfile().displayName

settings = {
    "Picture":False,
    "group":{},
    "SpamInvite":False,
    "changeCover":False,
    "changeVideo":False,
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":False,
 #   "restartPoint": null,
    "userMention":{},
    "timeRestart": {},
    "server": {},
    "simiSimi":{},
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
}

wait = {
    "Limit": 1,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":False,
    "contact":False,
    "invite":False,
    'autoJoin':True,
    'autoAdd':False,
    'autoBlock':False,
    'Timeline':True,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "mentionKick":False,
    "welcomeOn":True,
    "likeOn":True,
    "stickerOn":False,
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "myProfile": {
            "displayName": "",
            "coverId": "",
            "pictureStatus": "",
            "statusMessage": ""
            },
    "unsend":True,
    "mention":"Cie.......Yang lg ngintip mantan,,,?",
    "Respontag":"SI ANJING NGETAG",
    "welcome":"รεℓαɱαт ∂αтαɳɠ \nɓµ∂αყαҡαɳ ૮εҡ ɳσтε.\nรεɱoga jadi kawan baik\namin",
    "leave":"Slamat tinggal sobat\nsmoga ktmu di lain hari nanti",
    "comment":" ──────┅┅──────\nᴼᴾᴱᴺ ᴼᴿᴰᴱᴿ\n────────┅┅───────\n➣ꜱᴇʟꜰʙᴏᴛ ᴏɴʟʏ\nꜱᴇʟꜰʙᴏᴛ + ᴀꜱɪꜱᴛ\n1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ\n1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 2 ᴀꜱɪꜱᴛ\n1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 3 ᴀꜱɪꜱᴛ\n1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 4 ᴀꜱɪꜱᴛ\n1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 5 ᴀꜱɪꜱᴛ\nʙᴏᴛᴘʀᴏᴛᴇᴄᴛ 3-11 ʙᴏᴛ ᴀꜱɪꜱᴛ\nɴᴇᴡ ꜱᴄʀɪᴘᴛ\n─────────┅┅─────────\n  ✯C͜͡r͜͡e͜͡a͜͡t͜͡o͜͡r✯͜͡$͜͡ë͜͡I͜͡F͜͡-͜͡฿͜͜͡͡o͜͡t͜͡ ͜͡✯\nline.me/ti/p/~gerhanaselatan\nline.me/ti/p/~cyberline11\nѕєʟғвот κɪcκєʀ_+_ᴘʀᴏᴛᴇᴄᴛ\n────────┅☆͜͡┅────────",
    "message":"Terimɑ Kɑsih yɑ....\nUdɑh Menɑmbɑhkɑn Sɑyɑ Sebɑgɑi Temɑn ɑndɑ.\nSemogɑ Kitɑ Bisɑ Jɑlin pertemanan dengan baik\n\nвστ вy:gerhana",
}
read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

coverId = {}


lineProfile = cl.getProfile()
backup = cl.getProfile()
backup.displayName = lineProfile.displayName
backup.statusMessage = lineProfile.statusMessage
backup.pictureStatus = lineProfile.pictureStatus


with open('creator.json', 'r') as fp:
     creator = json.load(fp)
with open('owner.json', 'r') as fp:
     owner = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
f = codecs.open('Tblacklist.json','w','utf-8')
Setmain = json.load(Setbot)
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)

mulai = time.time()

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        ginfo = cl.getGroup(to)
        textx = "「 Daftar Member 」\n\n1. "
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "「✭」{}. ".format(str(no))
            else:
                textx += "\n「 Total {} Member 」".format(str(len(mid)))
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
           
def siderMembers(to, mid):
    try:
        arrData = ""
        textx = format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
         #       textx += "%i. " % (num)
                text += mention+"â Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\nâ Group : "+str(len(gid))+"\nâ Teman : "+str(len(teman))+"\nâ Expired : In "+hari+"\nâ Version : TETX-BOTS v11,5\nâ Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\nâ Runtime : \n â¢ "+bot
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "「 Auto Welcome 」\nɦαℓℓσ.......  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+" Di "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "「 Respon Leave 」\nBaper Ya Kak ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))


def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        ki.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
def delete_log1():
    ndt = datetime.now()
    for data in msg_dict1:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict1[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict1[msg_id]

def atend1():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict1, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "🔰➣ " + key + " [✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺--MΣΠU]🔰🔰\n" + \
                  "🔰➣" + key + "🔯✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺🔯\n" + \
                  "🔰➣" + key + "ʜᴇʟᴘ\n" + \
                  "🔰➣" + key + "ʜᴇʟᴘ1\n" + \
                  "🔰➣" + key + "ʜᴇʟᴘ2\n" + \
                  "🔰➣" + key + "ʜᴇʟᴘ3\n" + \
                  "🔰➣" + key + "ʜᴇʟᴘ4\n" + \
                  "🔰➣" + key + "ʜᴇʟᴘ5\n" + \
                  "🔰➣" + key + "ᴍᴇ\n" + \
                  "🔰➣" + key + "sᴛᴀᴛᴜs\n" + \
                  "🔰➣" + key + "ᴀʙᴏᴜᴛ\n" + \
                  "🔰➣" + key + "Cek bot\n" + \
                  "🔰➣" + key + "ʀᴇsᴛᴀʀᴛ\n" + \
                  "🔰➣" + key + "ʀᴜɴᴛɪᴍᴇ\n" + \
                  "🔰➣" + key + "ᴄʀᴇᴀᴛᴏʀ\n" + \
                  "🔰➣" + key + "sᴘᴇᴇᴅ/sᴘ\n" + \
                  "🔰➣" + key + "Bot:on\off\n" + \
                  "🔰➣" + key + "Staff:on\off\n" + \
                  "🔰➣" + key + "Admin on\off\n" + \
                  "🔰➣" + key + "Refresh\n" + \
                  "🔰➣" + key + "Cb/Cek limit bot\n" + \
                  "🔰➣" + key + "Masuk\n" + \
                  "🔰➣" + key + "Pulang/sᴘ\n" + \
                  "🔯「▶▶Kunci Protect▶▶」\n" + \
                  "🔰➣" + key + "Antijs stay\n" + \
                  "🔰➣" + key + "Jin\n" + \
                  "🔰➣" + key + "Jut\n" + \
                  "🔰➣" + key + "Ghost in\n" + \
                  "🔰➣" + key + "Terxbot\n" + \
                  "🔰➣" + key + "Reinvite\n" + \
                  "🔰➣" + key + "Buka\n" + \
                  "🔰➣" + key + "Tutup\n" + \
                  "🔰➣" + key + "Blc\n" + \
                  "🔰➣" + key + "Clearban.Cuci\n" + \
                  "🔰➣" + key + "Adminadd @\n" + \
                  "🔰➣ " + key + "Admindell @\n" + \
                  "🔰➣" + key + "protectkick on\off\n" + \
                  "🔰➣" + key + "protectjoin on\off\n" + \
                  "🔰➣" + key + "protectinvite on\off\n" + \
                  "🔰➣" + key + "protecturl on\off\n" + \
                  "🔰➣" + key + "Ghost on\off\n" + \
                  "🔰➣" + key + "Bot1,2,3,4up\n" + \
                  "🔰➣" + key + "Allpro on\off\n" + \
                  "🔰➣" + key + "Ajs on\n" + \
                  "🔰➣" + key + "ᴋɪᴄᴋᴀʟʟᴍᴇᴍʙᴇʀ)\n" + \
                  "🔰➣" + key + "ʙʀᴏᴀᴅᴄᴀsᴛ:「ᴛᴇxᴛ」\n" + \
                  "🔰➣" + key + "sᴇᴛᴋᴇʏ「ɴᴇᴡ ᴋᴇʏ」 \n" + \
                  "🔰➣" + key + "ᴍʏᴋᴇʏ\n" + \
                  "🔰➣" + key + "ʀᴇsᴇᴛᴋᴇʏ\n" + \
                  "🔰➣" + key + "ʀᴇғʀᴇsʜ\n" + \
                  "🔰➣" + key + "Reset\n"+ \
                  "🔰➣" + key + "Reset\n"+ \
                  "🔰🔰🔰✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺🔰🔰🔰"
              
    return helpMessage

def help1():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "🔰 " + key + " [✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺🔀MΣΠU]🔰\n" + \
                  "🔰" + key + "ᴛᴀɢᴀʟʟ/ɴᴀʜ\n" + \
                  "🔰" + key + "ɢɪɴғᴏ\n" + \
                  "🔰" + key + "ᴏᴘᴇɴ\n" + \
                  "🔰" + key + "ᴄʟᴏsᴇ\n" + \
                  "🔰" + key + "ᴜʀʟ\n" + \
                  "🔰" + key + "ɢʀᴜᴘʟɪsᴛ\n" + \
                  "🔰" + key + "Terxbot\n" + \
                  "🔰" + key + "Harga\n" + \
                  "🔰" + key + "Promo\n" + \
                  "🔰" + key + "ɪɴғᴏɢʀᴜᴘ「ɴᴏᴍᴇʀ」\n" + \
                  "🔰" + key + "ɪɴғᴏᴍᴇᴍ「ɴᴏᴍᴇʀ」\n" + \
                  "🔰" + key + "ʀᴇᴍᴏᴠᴇ ᴄʜᴀᴛ\n" + \
                  "🔰" + key + "ᴍɪᴅ「@」\n" + \
                  "🔰" + key + "sᴛᴇᴀʟ「@」\n" + \
                  "🔰" + key + "ᴄᴏᴠᴇʀ「@」\n" + \
                  "🔰" + key + "ᴄʟᴏɴᴇ「@」\n" + \
                  "🔰" + key + "ʀᴇsᴛᴏʀᴇ\n" + \
                  "🔰" + key + "ʙᴀᴄᴋᴜᴘ\n" + \
                  "🔰" + key + "ʀᴇᴊᴇᴄᴛ\n" + \
                  "🔰" + key + "sᴘᴀᴍᴄᴀʟʟᴛᴏ 「ᴊᴜᴍʟᴀʜ」 「@」\n" + \
                  "🔰" + key + "sᴘᴀᴍᴛᴀɢ:「ᴊᴜᴍʟᴀʜɴʏᴀ」\n" + \
                  "🔰" + key + "sᴘᴀᴍᴛᴀɢ「@」\n" + \
                  "🔰" + key + "sᴘᴀᴍᴄᴀʟʟ:「ᴊᴜᴍʟᴀʜɴʏᴀ」\n" + \
                  "🔰" + key + "sᴘᴀᴍᴄᴀʟʟ\n" + \
                  "🔰" + key + "ᴍʏɴᴀᴍᴇ:「ɴᴀᴍᴀ」\n" + \
                  "🔰" + key + "ᴄᴘᴘ「ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ」\n" + \
                  "🔰" + key + "ᴄᴠᴘ 「ᴋɪʀɪᴍ ᴠɪᴅᴇᴏɴʏᴀ」\n" + \
                  "🔰" + key + "ᴜᴘᴅᴀᴛᴇɢʀᴜᴘ\n" + \
                  "🔰" + key + "ɢɪғᴛ:「ᴍɪᴅ ᴋᴏʀʙᴀɴ」「ᴊᴜᴍʟᴀʜ」\n" + \
                  "🔰" + key + "sᴘᴀᴍ:「ᴍɪᴅ ᴋᴏʀʙᴀɴ」「ᴊᴜᴍʟᴀʜ」\n" + \
                  "🔰🔰🔰「」↪  ʙʏ:✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺ ↩ 🔰🔰🔰\n" + \
                  "🔀 Creator:  https://line.me/ti/p/~kaway27"
                  
    return helpMessage1

def help2():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2= "🎞🎞「🔳SΣTTIΠG✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺ 🔳」🎞🎞\n" + \
                  "🎴➣ " + key + "ɪɴᴠɪᴛᴇ「ᴏɴ/ᴏғғ」\n" + \
                  "🎴➣ " + key + "sᴛɪᴄᴋᴇʀ「ᴏɴ/ᴏғғ」\n" + \
                  "🎴➣" + key + "ᴜɴsᴇɴᴅ「ᴏɴ/ᴏғғ」\n" + \
                  "🎴➣ " + key + "sɪᴅᴇʀ「ᴏɴ/ᴏғғ」\n" + \
                  "🎴➣" + key + "ʀᴇsᴘᴏɴ「ᴏɴ/ᴏғғ」\n" + \
                  "🎴➣ " + key + "ᴛɪᴍᴇʟɪɴᴇ「ᴏɴ/ᴏғғ」\n" + \
                  "🎴➣ " + key + "ᴄᴏɴᴛᴀᴄᴛ「ᴏɴ/ᴏғғ」\n" + \
                  "🎴➣ " + key + "ᴀᴜᴛᴏᴊᴏɪɴ「ᴏɴ/ᴏғғ」\n" + \
                  "🎴➣ " + key + "ᴀᴜᴛᴏᴀᴅᴅ「ᴏɴ/ᴏғғ」\n" + \
                  "🎴➣ " + key + "ᴡᴇʟᴄᴏᴍᴇ「ᴏɴ/ᴏғғ」\n" + \
                  "🎴➣ " + key + "ᴀᴜᴛᴏʟᴇᴀᴠᴇ「ᴏɴ/ᴏғғ」\n" + \
                  "🎴➣ " + key + "ᴊᴏɪɴᴛɪᴄᴋᴇᴛ「ᴏɴ/ᴏғғ」\n" + \
                  "🎴➣ " + key + "ᴄᴇᴋ sɪᴅᴇʀ\n" + \
                  "🎴➣ " + key + "ᴄᴇᴋ sᴘᴀᴍ\n" + \
                  "🎴➣ " + key + "ᴄᴇᴋ ᴘᴇsᴀɴ  \n" + \
                  "🎴➣ " + key + "ᴄᴇᴋ ʀᴇsᴘᴏɴ \n" + \
                  "🎴➣ " + key + "ᴄᴇᴋ ʟᴇᴀᴠᴇ\n" + \
                  "🎴➣ " + key + "ᴄᴇᴋ ᴡᴇʟᴄᴏᴍᴇ\n" + \
                  "🎴➣ " + key + "sᴇᴛ sɪᴅᴇʀ:「ᴛᴇxᴛ」\n" + \
                  "🎴➣ " + key + "sᴇᴛ sᴘᴀᴍ:「ᴛᴇxᴛ」」\n" + \
                  "🎴➣ " + key + "sᴇᴛ ᴘᴇsᴀɴ:「ᴛᴇxᴛ」\n" + \
                  "🎴➣ " + key + "sᴇᴛ ʀᴇsᴘᴏɴ:「ᴛᴇxᴛ」\n" + \
                  "🎴➣ " + key + "sᴇᴛ ʟᴇᴀᴠᴇ:「ᴛᴇxᴛ」\n" + \
                  "🎴➣ " + key + "sᴇᴛ ᴡᴇʟᴄᴏᴍᴇ:「ᴛᴇxᴛ」\n" + \
                  " 🎞🎞🎞🎞✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺]🎞🎞🎞🎞\n" + \
                  "✅Creator:  https:.//line.me/ti/p/~kaway27"

    return helpMessage2

def help3():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage3 = "🔀🔀「🔄MΣDIΔ ✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺🔄」🔀🔀\n" + \
                  "↪ " + key + "Musik「Nama Penyanyi」\n" + \
                  "↪ " + key + "Listmp3\n" + \
                  "↪ " + key + "Addmp3「Teks」\n" + \
                  "↪ " + key + "Dellmp3「Teks」\n" + \
                  "🔀▶      「✭VIDEO TERX✭」\n" + \
                  "↪ " + key + "Listvideo\n" + \
                  "↪ " + key + "Addvideo「Teks」\n" + \
                  "↪ " + key + "Dellvideo「Teks」\n" + \
                  "🔀▶      「✭GAMBAR TERX✭」\n" + \
                  "↪ " + key + "Listimage\n" + \
                  "↪ " + key + "Addimg「Teks」\n" + \
                  "↪ " + key + "Dellimg「Teks」\n" + \
                  "🔀▶      「✭STICKER TERX✭」\n" + \
                  "↪ " + key + "Liststicker\n" + \
                  "↪ " + key + "Addsticker「Teks」\n" + \
                  "↪ " + key + "Dellsticker「Teks」\n" + \
                  "↪ " + key + "Kode wilayah\n" + \
                  "🔀▶      「✭MEDIA LAIN ✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺✭」\n" + \
                  "↪ " + key + "Lihat 「Kode wilayah cctv」\n" + \
                  "↪ " + key + "Youtube「Query」\n" + \
                  "↪ " + key + "Get-fs「Query」\n" + \
                  "↪ " + key + "Get-line「ID Line」\n" + \
                  "↪ " + key + "Get-apk「Query」\n" + \
                  "↪ " + key + "Get-gif「Query」\n" + \
                  "↪ " + key + "Get-xxx「Query」\n" + \
                  "↪ " + key + "Get-anime「Query」\n" + \
                  "↪ " + key + "Get-mimpi「Query」\n" + \
                  "↪ " + key + "Get-audio「Query」\n" + \
                  "↪  " + key + "Get-mp3「Query」\n" + \
                  "↪"  + key + "Get-video「Query」\n" + \
                  "↪ " + key + "Get-bintang「Zodiak」\n" + \
                  "↪ " + key + "Get-zodiak「Zodiak」\n" + \
                  "↪ " + key + "Get-sholat「Nama Kota」\n" + \
                  "↪ " + key + "Get-cuaca「Nama Kota」\n" + \
                  "↪ " + key + "Get-lokasi「Nama Kota」\n" + \
                  "↪ " + key + "Get-lirik「Judul Lagu」\n" + \
                  "↪ " + key + "Get-instagram「User Name」\n" + \
                  "↪ " + key + "Cekdate「tgl-bln-thn」\n" + \
                  "🔀▶➖✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺➖\n" + \
                  "✅  Creator:  https://line.me/ti/p/~kaway27"

    return helpMessage3

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return

        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                            cl.kickoutFromGroup(op.param1,[op.param2])                  
                            cl.updateGroup(X)                                       
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                ki.updateGroup(X)                                                   
                                ki.kickoutFromGroup(op.param1,[op.param2])                                                                              
                    except:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kk.updateGroup(X)    
                                    kk.kickoutFromGroup(op.param1,[op.param2])                                              
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        kc.updateGroup(X)                                                                              
                                        kc.kickoutFromGroup(op.param1,[op.param2])                                                                                                                         
                            except: 
                                try:
                                    if kb.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            kb.reissueGroupTicket(op.param1)
                                            X = kb.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            kb.updateGroup(X)
                                            kb.kickoutFromGroup(op.param1,[op.param2])                                                                                   
                                except:
                                    try:
                                        if kd.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                kd.reissueGroupTicket(op.param1)
                                                X = kd.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                kd.updateGroup(X)
                                                kd.kickoutFromGroup(op.param1,[op.param2])                                                                
                                    except:
                                        try:
                                            if ke.getGroup(op.param1).preventedJoinByTicket == False:
                                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                    ke.reissueGroupTicket(op.param1)
                                                    X = ke.getGroup(op.param1)
                                                    X.preventedJoinByTicket = True
                                                    ke.updateGroup(X)
                                                    ke.kickoutFromGroup(op.param1,[op.param2])                                                                                                    
                                        except:
                                            try:
                                                if kf.getGroup(op.param1).preventedJoinByTicket == False:
                                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                        kf.reissueGroupTicket(op.param1)
                                                        X = kf.getGroup(op.param1)
                                                        X.preventedJoinByTicket = True
                                                        kf.updateGroup(X)
                                                        kf.kickoutFromGroup(op.param1,[op.param2])                                                                                                             
                                            except:
                                                try:
                                                    if kj.getGroup(op.param1).preventedJoinByTicket == False:
                                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                            kj.reissueGroupTicket(op.param1)
                                                            X = kj.getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            kj.updateGroup(X)                                                         
                                                            kj.kickoutFromGroup(op.param1,[op.param2])                                                                
                                                except:
                                                    try:
                                                        if sw.getGroup(op.param1).preventedJoinByTicket == False:
                                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                sw.reissueGroupTicket(op.param1)                                                            
                                                                sw.kickoutFromGroup(op.param1,[op.param2]) #y
                                                                X = sw.getGroup(op.param1)
                                                                X.preventedJoinByTicket = True
                                                                sw.updateGroup(X)
                                                                sw.kickoutFromGroup(op.param1,[op.param2])                                                                                                                                                              
                                                    except:
                                                        pass
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)              

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)       
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)               
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)         
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)          
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        kb.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kd.acceptGroupInvitation(op.param1)
                        ginfo = kd.getGroup(op.param1)              
                        kd.leaveGroup(op.param1)
                    else:
                        kd.acceptGroupInvitation(op.param1)
                        ginfo = kd.getGroup(op.param1)                   
            if Fmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)                
                        ke.leaveGroup(op.param1)
                    else:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)         
            if Gmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kf.acceptGroupInvitation(op.param1)
                        ginfo = kf.getGroup(op.param1)
                        kf.leaveGroup(op.param1)
                    else:
                        kf.acceptGroupInvitation(op.param1)
                        ginfo = kf.getGroup(op.param1)                                   

        if op.type == 13: 
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = ki.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            ki.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = kk.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                kk.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = kc.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    kc.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = kb.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        kb.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    try:
                                        group = kd.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            kd.cancelGroupInvitation(op.param1,[_mid])
                                    except:
                                        try:
                                            group = ke.getGroup(op.param1)
                                            gMembMids = [contact.mid for contact in group.invitee]
                                            for _mid in gMembMids:
                                                ke.cancelGroupInvitation(op.param1,[_mid])
                                        except:
                                            try:
                                                group = kf.getGroup(op.param1)
                                                gMembMids = [contact.mid for contact in group.invitee]
                                                for _mid in gMembMids:
                                                    kf.cancelGroupInvitation(op.param1,[_mid])
                                            except:
                                                try:
                                                    group = kj.getGroup(op.param1)
                                                    gMembMids = [contact.mid for contact in group.invitee]
                                                    for _mid in gMembMids:
                                                        kj.cancelGroupInvitation(op.param1,[_mid])
                                                except:
                                                    try:
                                                        group = sw.getGroup(op.param1)
                                                        gMembMids = [contact.mid for contact in group.invitee]
                                                        for _mid in gMembMids:
                                                            sw.cancelGroupInvitation(op.param1,[_mid])
                                                    except:
                                                        try:
                                                            group = cl.getGroup(op.param1)
                                                            gMembMids = [contact.mid for contact in group.invitee]
                                                            for _mid in gMembMids:
                                                                cl.cancelGroupInvitation(op.param1,[_mid])
                                                        except:                                                                       
                                                            pass

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                    
        if op.type == 13:
            if op.param2 in wait["blacklist"]:        
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                    
        if op.type == 13:
            if op.param3 in wait["blacklist"]:         
                    try:
                        random.choice(ABC).cancelGroupInvitation(op.param1,[op.param3])
                    except:
                        pass
 
        if op.type == 17:  #sadis
            if op.param2 in wait["blacklist"]:       
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)
                
        if op.type == 17:
            if op.param1 in left:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leftMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)
                sendMention(to, "ãAuto Mentionã\nâ«@!", [sender])
                cl.sendContact(to, sender)         
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    f = codecs.open('Terxblacklist.json','w','utf-8')
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	f = codecs.open('Terxblacklist.json','w','utf-8')
                        	ki.kickoutFromGroup(op.param1,[op.param2])                                                                                              
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:                       
                                ki.kickoutFromGroup(op.param1,[op.param2])    
                                ki.cancelGroupInvitation(op.param1,[op.param3]) #y                          
                                ki.acceptGroupInvitation(op.param1) 
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:                 
                                    kk.kickoutFromGroup(op.param1,[op.param2])                            
                                    kk.cancelGroupInvitation(op.param1,[op.param3])                    
                                    kk.acceptGroupInvitation(op.param1) 
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:             
                                        kc.kickoutFromGroup(op.param1,[op.param2])                       
                                        kc.cancelGroupInvitation(op.param1,[op.param3]) 
                                        kc.acceptGroupInvitation(op.param1) 
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            kb.kickoutFromGroup(op.param1,[op.param2])                                                       
                                            kb.cancelGroupInvitation(op.param1,[op.param3]) 
                                            kb.acceptGroupInvitation(op.param1) 
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                kd.kickoutFromGroup(op.param1,[op.param2])                                        
                                                kd.cancelGroupInvitation(op.param1,[op.param3])
                                                kd.acceptGroupInvitation(op.param1) 
                                        except:
                                            try:
                                                if op.param3 not in wait["blacklist"]:
                                                    ke.kickoutFromGroup(op.param1,[op.param2])                                               
                                                    ke.cancelGroupInvitation(op.param1,[op.param3]) 
                                                    ke.acceptGroupInvitation(op.param1) 
                                            except:
                                               try:
                                                   if op.param3 not in wait["blacklist"]:
                                                       kj.kickoutFromGroup(op.param1,[op.param2])                                                  
                                                       kj.cancelGroupInvitation(op.param1,[op.param3]) 
                                                       kj.acceptGroupInvitation(op.param1) 
                                               except:
                                                  try:
                                                      if op.param3 not in wait["blacklist"]:
                                                          kf.kickoutFromGroup(op.param1,[op.param2])                                                       
                                                          kf.cancelGroupInvitation(op.param1,[op.param3]) 
                                                          kf.acceptGroupInvitation(op.param1) 
                                                  except:
                                                     try:
                                                         if op.param3 not in wait["blacklist"]:
                                                             sw.kickoutFromGroup(op.param1,[op.param2])                                                   
                                                             sw.cancelGroupInvitation(op.param1,[op.param2])
                                                             sw.acceptGroupInvitation(op.param1) 
        
                                                     except:
                                                        try:
                                                            if op.param3 not in wait["blacklist"]:
                                                                ki.kickoutFromGroup(op.param1,[op.param2])                                                  
                                                                ki.cancelGroupInvitation(op.param1,[op.param3])
                                                                cl.acceptGroupInvitation(op.param1) 
                                                        except:
                                                            try:
                                                                if op.param3 not in wait["blacklist"]:
                                                                    kk.kickoutFromGroup(op.param1,[op.param2])                                                        
                                                                    kk.cancelGroupInvitation(op.param1,[op.param3]) 
                                                                    cl.acceptGroupInvitation(op.param1) 
                                                            except:
                                                               try:
                                                                   if op.param3 not in wait["blacklist"]:
                                                                       kc.kickoutFromGroup(op.param1,[op.param2])                                                                    
                                                                       kc.cancelGroupInvitation(op.param1,[op.param3])                                                         
                                                                       cl.acceptGroupInvitation(op.param1) 
                                                               except:
                                                                  try:
                                                                      if op.param3 not in wait["blacklist"]:
                                                                          kb.kickoutFromGroup(op.param1,[op.param2])                                                                 
                                                                          kb.cancelGroupInvitation(op.param1,[op.param3])                                                
                                                                          cl.acceptGroupInvitation(op.param1) 
  
                                                                  except:
                                                                     try:
                                                                         if op.param3 not in wait["blacklist"]:
                                                                             kd.kickoutFromGroup(op.param1,[op.param2])                      
                                                                             kd.cancelGroupInvitation(op.param1,[op.param3])                                                     
                                                                             cl.acceptGroupInvitation(op.param1) 
                                                                     except:
                                                                        try:
                                                                            if op.param3 not in wait["blacklist"]:
                                                                                ke.kickoutFromGroup(op.param1,[op.param2])                                                                        
                                                                                ke.cancelGroupInvitation(op.param1,[op.param3])                                                                         
                                                                                cl.acceptGroupInvitation(op.param1) 
                                                                        except:
                                                                           try:
                                                                               if op.param3 not in wait["blacklist"]:
                                                                                    kj.kickoutFromGroup(op.param1,[op.param2])                                                                            
                                                                                    kj.cancelGroupInvitation(op.param1,[op.param3])                                                                   
                                                                                    cl.acceptGroupInvitation(op.param1) 
                                                                           except:
                                                                               pass  
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, wait["message"])

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                else:
                	pass

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = ki.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            random.choice(ki).cancelGroupInvitation(op.param1,[op.param3])
                            random.choice(kk).kickoutFromGroup(op.param1,[op.param2])                                                   
                    except:
                        try:
                            group = kk.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                            	random.choice(kk).cancelGroupInvitation(op.param1,[op.param3])                                                                                                                                                                                                     
                        except:
                            try:
                                group = kc.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    random.choice(kc).cancelGroupInvitation(op.param1,[op.param3])                                                           
                                    random.choice(kb).kickoutFromGroup(op.param1,[op.param2])                                                                                                               
                            except:
                                try:
                                    group = kb.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                    	random.choice(kb).cancelGroupInvitation(op.param1,[op.param3])                                                                                                                    
                                except:
                                    try:
                                        group = kd.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            random.choice(kd).cancelGroupInvitation(op.param1,[op.param3])                                     
                                            random.choice(ke).kickoutFromGroup(op.param1,[op.param2])                                                                
                                    except:
                                        try:
                                            group = ke.getGroup(op.param1)
                                            gMembMids = [contact.mid for contact in group.invitee]
                                            for _mid in gMembMids:
                                            	random.choice(ke).cancelGroupInvitation(op.param1,[op.param3])                                                                                                                                   
                                        except:
                                            try:
                                                group = kf.getGroup(op.param1)
                                                gMembMids = [contact.mid for contact in group.invitee]
                                                for _mid in gMembMids:
                                                    random.choice(kf).cancelGroupInvitation(op.param1,[op.param3])                                          
                                                    random.choice(kf).kickoutFromGroup(op.param1,[op.param2])                                                                  
                                            except:
                                            	pass                    
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass
                
        if op.type == 19:
            if op.param1 in ghost:
                try:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)                                     
                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.cancelGroupInvitation(op.param1,[op.param2])
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        sw.findAndAddContactsByMid(op.param3)
                        sw.inviteIntoGroup(op.param1,[op.param3])                           
                        cl.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                        kk.acceptGroupInvitation(op.param1)
                        kc.acceptGroupInvitation(op.param1)
                        kb.acceptGroupInvitation(op.param1)
                        kd.acceptGroupInvitation(op.param1)
                        ke.acceptGroupInvitation(op.param1)
                        kf.acceptGroupInvitation(op.param1)    
                        X = cl.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
                        sw.leaveGroup(op.param1)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True        
                except:
                    try:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            G = kk.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            kk.updateGroup(G)
                            invsend = 0
                            Ticket = kk.reissueGroupTicket(op.param1)            
                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param3)
                            ki.inviteIntoGroup(op.param1,[op.param3])        
                            ki.cancelGroupInvitation(op.param1,[op.param2]) ####
                            cl.acceptGroupInvitation(op.param1)
                            ki.acceptGroupInvitation(op.param1)
                            kk.acceptGroupInvitation(op.param1)
                            kc.acceptGroupInvitation(op.param1)
                            kb.acceptGroupInvitation(op.param1)
                            kd.acceptGroupInvitation(op.param1)
                            ke.acceptGroupInvitation(op.param1)
                            kf.acceptGroupInvitation(op.param1)
                            X = ki.getGroup(op.param1)
                            X.preventedJoinByTicket = True        
                            ki.updateGroup(X)                      
                            cl.inviteIntoGroup(op.param1,[Jmid])
                            random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                            wait["blacklist"][op.param2] = True        
                    except:
                        try:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                G = kc.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                kc.updateGroup(G)
                                invsend = 0
                                Ticket = kc.reissueGroupTicket(op.param1)                   
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.cancelGroupInvitation(op.param1,[op.param2]) ####
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param3)
                                kk.inviteIntoGroup(op.param1,[op.param3])                           
                                cl.acceptGroupInvitation(op.param1)
                                ki.acceptGroupInvitation(op.param1)
                                kk.acceptGroupInvitation(op.param1)
                                kc.acceptGroupInvitation(op.param1)
                                kb.acceptGroupInvitation(op.param1)
                                kd.acceptGroupInvitation(op.param1)
                                ke.acceptGroupInvitation(op.param1)
                                kf.acceptGroupInvitation(op.param1)        
                                X = kk.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                kk.updateGroup(X)                       
                                kk.inviteIntoGroup(op.param1,[Zmid])   
                                random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                wait["blacklist"][op.param2] = True        
             
                        except:
                            try:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    G = kb.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kb.updateGroup(G)
                                    invsend = 0
                                    Ticket = kb.reissueGroupTicket(op.param1)                      
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.cancelGroupInvitation(op.param1,[op.param2]) 
                                    kc.kickoutFromGroup(op.param1,[op.param2])                                 
                                    kc.findAndAddContactsByMid(op.param3)
                                    kc.inviteIntoGroup(op.param1,[op.param3])                
                                    cl.acceptGroupInvitation(op.param1)
                                    ki.acceptGroupInvitation(op.param1)
                                    kk.acceptGroupInvitation(op.param1)
                                    kc.acceptGroupInvitation(op.param1)
                                    kb.acceptGroupInvitation(op.param1)
                                    kd.acceptGroupInvitation(op.param1)
                                    ke.acceptGroupInvitation(op.param1)
                                    kf.acceptGroupInvitation(op.param1)
                                    X = kb.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kb.updateGroup(X)                                   
                                    kb.inviteIntoGroup(op.param1,[Jmid]) 
                                    random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                    wait["blacklist"][op.param2] = True        
                          
                            except:
                                try:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        G = kd.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        kd.updateGroup(G)
                                        invsend = 0
                                        Ticket = kd.reissueGroupTicket(op.param1)                               
                                        kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kb.cancelGroupInvitation(op.param1,[op.param2]) # 
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param3)
                                        kb.inviteIntoGroup(op.param1,[op.param3])                          
                                        cl.acceptGroupInvitation(op.param1)
                                        ki.acceptGroupInvitation(op.param1)
                                        kk.acceptGroupInvitation(op.param1)
                                        kc.acceptGroupInvitation(op.param1)
                                        kb.acceptGroupInvitation(op.param1)
                                        kd.acceptGroupInvitation(op.param1)
                                        ke.acceptGroupInvitation(op.param1)
                                        kf.acceptGroupInvitation(op.param1)                    
                                        X = kd.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        kd.updateGroup(X)                   
                                        kd.inviteIntoGroup(op.param1,[Zmid])
                                        random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                        wait["blacklist"][op.param2] = True        
                                except:
                                    try:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            G = ke.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            ke.updateGroup(G)
                                            invsend = 0
                                            Ticket = ke.reissueGroupTicket(op.param1)              
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.cancelGroupInvitation(op.param1,[op.param2]) # 
                                            kd.kickoutFromGroup(op.param1,[op.param2])             
                                            kd.findAndAddContactsByMid(op.param3)
                                            kd.inviteIntoGroup(op.param1,[op.param3])                                                                                                
                                            cl.acceptGroupInvitation(op.param1)
                                            ki.acceptGroupInvitation(op.param1)
                                            kk.acceptGroupInvitation(op.param1)
                                            kc.acceptGroupInvitation(op.param1)
                                            kb.acceptGroupInvitation(op.param1)
                                            kd.acceptGroupInvitation(op.param1)
                                            ke.acceptGroupInvitation(op.param1)
                                            kf.acceptGroupInvitation(op.param1)
                                            X = ke.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            ke.updateGroup(X)                                 
                                            ke.inviteIntoGroup(op.param1,[Jmid])
                                            random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])   
                                            wait["blacklist"][op.param2] = True                                                                                   
                                    except:
                                        try:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                G = kf.getGroup(op.param1)
                                                G.preventedJoinByTicket = False
                                                kf.updateGroup(G)
                                                invsend = 0
                                                Ticket = kf.reissueGroupTicket(op.param1)                           
                                                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                ke.cancelGroupInvitation(op.param1,[op.param2]) # 
                                                ke.kickoutFromGroup(op.param1,[op.param2])     
                                                ke.findAndAddContactsByMid(op.param3)
                                                ke.inviteIntoGroup(op.param1,[op.param3])              
                                                cl.acceptGroupInvitation(op.param1)
                                                ki.acceptGroupInvitation(op.param1)
                                                kk.acceptGroupInvitation(op.param1)
                                                kc.acceptGroupInvitation(op.param1)
                                                kb.acceptGroupInvitation(op.param1)
                                                kd.acceptGroupInvitation(op.param1)
                                                ke.acceptGroupInvitation(op.param1)
                                                kf.acceptGroupInvitation(op.param1)  
                                                X = kf.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                kf.updateGroup(X)                                               
                                                kf.inviteIntoGroup(op.param1,[Zmid])
                                                random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                                wait["blacklist"][op.param2] = True        
                                         
                                        except:
                                            try:
                                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                    G = cl.getGroup(op.param1)
                                                    G.preventedJoinByTicket = False
                                                    cl.updateGroup(G)
                                                    invsend = 0
                                                    Ticket = cl.reissueGroupTicket(op.param1)                                                                   
                                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                    kf.cancelGroupInvitation(op.param1,[op.param2]) # 
                                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                                    kf.findAndAddContactsByMid(op.param3)
                                                    kf.inviteIntoGroup(op.param1,[op.param3])                                          
                                                    cl.acceptGroupInvitation(op.param1)
                                                    ki.acceptGroupInvitation(op.param1)
                                                    kk.acceptGroupInvitation(op.param1)
                                                    kc.acceptGroupInvitation(op.param1)
                                                    kb.acceptGroupInvitation(op.param1)
                                                    kd.acceptGroupInvitation(op.param1)
                                                    ke.acceptGroupInvitation(op.param1)
                                                    kf.acceptGroupInvitation(op.param1)     
                                                    X = cl.getGroup(op.param1)
                                                    X.preventedJoinByTicket = True
                                                    cl.updateGroup(X)                                         
                                                    cl.inviteIntoGroup(op.param1,[Jmid])
                                                    random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                                    wait["blacklist"][op.param2] = True        
                                                  
                                            except:
                                                try:
                                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                        G = ki.getGroup(op.param1)
                                                        G.preventedJoinByTicket = False
                                                        ki.updateGroup(G)
                                                        invsend = 0
                                                        Ticket = ki.reissueGroupTicket(op.param1)                 
                                                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                        sw.cancelGroupInvitation(op.param1,[op.param2]) # 
                                                        sw.kickoutFromGroup(op.param1,[op.param2])
                                                        sw.findAndAddContactsByMid(op.param3)
                                                        sw.inviteIntoGroup(op.param1,[op.param3])                                                   
                                                        cl.acceptGroupInvitation(op.param1)
                                                        ki.acceptGroupInvitation(op.param1)
                                                        kk.acceptGroupInvitation(op.param1)
                                                        kc.acceptGroupInvitation(op.param1)
                                                        kb.acceptGroupInvitation(op.param1)
                                                        kd.acceptGroupInvitation(op.param1)
                                                        ke.acceptGroupInvitation(op.param1)
                                                        kf.acceptGroupInvitation(op.param1) 
                                                        X = cl.getGroup(op.param1)
                                                        X.preventedJoinByTicket = True                                                      
                                                        cl.updateGroup(X)      
                                                        sw.leaveGroup(op.param1)
                                                        cl.inviteIntoGroup(op.param1,[Zmid]) 
                                                        random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])   
                                                        wait["blacklist"][op.param2] = True   
                                                        
     
                                                 
                                                except:
                                                    try:
                                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                            G = kk.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            kk.updateGroup(G)
                                                            invsend = 0
                                                            Ticket = kk.reissueGroupTicket(op.param1)                                                       
                                                            kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kj.cancelGroupInvitation(op.param1,[op.param2]) # 
                                                            kj.kickoutFromGroup(op.param1,[op.param2])
                                                            kj.findAndAddContactsByMid(op.param3)
                                                            kj.inviteIntoGroup(op.param1,[op.param3])                                                         
                                                            cl.acceptGroupInvitation(op.param1)
                                                            ki.acceptGroupInvitation(op.param1)
                                                            kk.acceptGroupInvitation(op.param1)
                                                            kc.acceptGroupInvitation(op.param1)
                                                            kb.acceptGroupInvitation(op.param1)
                                                            kd.acceptGroupInvitation(op.param1)
                                                            ke.acceptGroupInvitation(op.param1)
                                                            kf.acceptGroupInvitation(op.param1)                                                       
                                                            X = cl.getGroup(op.param1)
                                                            X.preventedJoinByTicket = True 
                                                            cl.updateGroup(X)    
                                                            kj.leaveGroup(op.param1)
                                                            cl.inviteIntoGroup(op.param1,[Jmid])                                    
                                                            random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])          
                                                            wait["blacklist"][op.param2] = True        
                                                                                                                                                           
                                                    except:
                                                        pass
                  
        if op.type == 19: 
            try:
                if op.param1 in protectantijs:
                  if op.param3 in mid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        sw.acceptGroupInvitation(op.param1)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                        sw.leaveGroup(op.param1)
                        cl.findAndAddContactsByMid(op.param1,[Zmid])
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.inviteIntoGroup(op.param1,[admin])
                    else:
                        pass
                        
                if op.param3 in Zmid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.findAndAddContactsByMid(op.param3)
                        ki.inviteIntoGroup(op.param1,[Zmid])
                        cl.sendMessage(op.param1,"Antijs")
                    else: #
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.findAndAddContactsByMid(op.param3)
                        kk.inviteIntoGroup(op.param1,[Zmid])
                        kk.sendMessage(op.param1,"Antijs")
                        
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.findAndAddContactsByMid(op.param3)
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            cl.sendMessage(op.param1,"=Admin Invited=")
                else:
                    pass
            except:
                pass
                
        if op.type == 32:
            if op.param1 in protectcancel:
              if op.param3 in Bots:    
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                    except:
                        pass
         
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.cancelGroupInvitation(op.param1,[op.param2]) #
                            wait["blacklist"][op.param2] = True
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.cancelGroupInvitation(op.param1,[op.param2]) #
                                wait["blacklist"][op.param2] = True
                        except:
                            try: 
                                if op.param3 not in wait["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.cancelGroupInvitation(op.param1,[op.param2]) #
                                    wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.cancelGroupInvitation(op.param1,[op.param2]) #
                                        wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.cancelGroupInvitation(op.param1,[op.param2]) #
                                            wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                ke.cancelGroupInvitation(op.param1,[op.param2]) #
                                                wait["blacklist"][op.param2] = True
                                        except:
                                            pass                                                                                  
                return

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])                 
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        ki.cancelGroupInvitation(op.param1,[op.param2]) #                     
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            kk.cancelGroupInvitation(op.param1,[op.param2]) #            
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                kc.cancelGroupInvitation(op.param1,[op.param2]) #                     
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    kb.cancelGroupInvitation(op.param1,[op.param2]) #                           
                                    cl.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                        kd.cancelGroupInvitation(op.param1,[op.param2]) #                             
                                        cl.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = ki.getGroup(op.param1)
                                            G.preventedJoinByTicket = False                           
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            ki.updateGroup(G)
                                            Ticket = ki.reissueGroupTicket(op.param1)                                 
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = ki.getGroup(op.param1)
                                            G.preventedJoinByTicket = True                  
                                            Ticket = ki.reissueGroupTicket(op.param1)                   
                                            ki.updateGroup(G)
            
                                        except:
                                            try:
                                                kk.kickoutFromGroup(op.param1,[op.param2])
                                                kk.inviteIntoGroup(op.param1,[op.param3])
                                                kk.cancelGroupInvitation(op.param1,[op.param2]) #                                            
                                                cl.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                                    kc.cancelGroupInvitation(op.param1,[op.param2]) #                                             
                                                    cl.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                                        kb.cancelGroupInvitation(op.param1,[op.param2]) #                                               
                                                        cl.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                                            kd.inviteIntoGroup(op.param1,[op.param3])
                                                            kd.cancelGroupInvitation(op.param1,[op.param2]) #                                                    
                                                            cl.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        ki.cancelGroupInvitation(op.param1,[op.param2]) #    
                        ki.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            kc.cancelGroupInvitation(op.param1,[op.param2]) #                      
                            ki.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,[op.param3])
                                kb.cancelGroupInvitation(op.param1,[op.param2]) #                      
                                ki.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                    kd.cancelGroupInvitation(op.param1,[op.param2]) #                           
                                    ki.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                        ke.cancelGroupInvitation(op.param1,[op.param2]) #                            
                                        ki.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = ki.getGroup(op.param1)
                                            G.preventedJoinByTicket = False                                                              
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            ki.updateGroup(G)                        
                                            Ticket = ki.reissueGroupTicket(op.param1)                                       
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = ki.getGroup(op.param1)
                                            G.preventedJoinByTicket = True                     
                                            Ticket = ki.reissueGroupTicket(op.param1)      
                                            ki.updateGroup(G)
                                        except:
                                            try:
                                                kd.kickoutFromGroup(op.param1,[op.param2])
                                                kd.inviteIntoGroup(op.param1,[op.param3])
                                                kd.cancelGroupInvitation(op.param1,[op.param2]) #                                          
                                                ki.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                                    ke.cancelGroupInvitation(op.param1,[op.param2]) #                                                                                        
                                                    ki.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                                        kf.cancelGroupInvitation(op.param1,[op.param2]) #                                   
                                                        ki.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                                            kk.cancelGroupInvitation(op.param1,[op.param2]) #                                                       
                                                            ki.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:               
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        kk.cancelGroupInvitation(op.param1,[op.param2]) #                
                        kk.acceptGroupInvitation(op.param1)
                    except:
                        try:                  
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                            kb.cancelGroupInvitation(op.param1,[op.param2]) #                     
                            kk.acceptGroupInvitation(op.param1)
                        except:
                            try:                    
                                kd.kickoutFromGroup(op.param1,[op.param2])
                                kd.inviteIntoGroup(op.param1,[op.param3])
                                kd.cancelGroupInvitation(op.param1,[op.param2]) #                      
                                kk.acceptGroupInvitation(op.param1)
                            except:
                                try:                         
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                    ke.cancelGroupInvitation(op.param1,[op.param2]) #                      
                                    kk.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                        kf.cancelGroupInvitation(op.param1,[op.param2])                          
                                        kk.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = kk.getGroup(op.param1)
                                            G.preventedJoinByTicket = False                    
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            kk.updateGroup(G)                             
                                            Ticket = kk.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kc.getGroup(op.param1)
                                            G.preventedJoinByTicket = True                                        
                                            G.preventedJoinByTicket = True
                                            kc.updateGroup(G)
                                            Ticket = kc.reissueGroupTicket(op.param1)                                    
                                        except:
                                            try:
                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                ki.cancelGroupInvitation(op.param1,[op.param2]) #                                           
                                                kk.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                                    kc.cancelGroupInvitation(op.param1,[op.param2]) #                          
                                                    kk.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                                        cl.cancelGroupInvitation(op.param1,[op.param2]) #                                   
                                                        kk.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                                            ke.cancelGroupInvitation(op.param1,[op.param2]) #                                              
                                                            kk.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kc.cancelGroupInvitation(op.param1,[op.param2]) #            
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kd.kickoutFromGroup(op.param1,[op.param2])
                            kd.inviteIntoGroup(op.param1,[op.param3])
                            kd.cancelGroupInvitation(op.param1,[op.param2]) #                    
                            kc.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ke.kickoutFromGroup(op.param1,[op.param2])
                                ke.inviteIntoGroup(op.param1,[op.param3])
                                ke.cancelGroupInvitation(op.param1,[op.param2])                           
                                kc.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                    kf.inviteIntoGroup(op.param1,[op.param3])
                                    kf.cancelGroupInvitation(op.param1,[op.param2]) #                            
                                    kc.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        ki.cancelGroupInvitation(op.param1,[op.param2]) #                         
                                        kc.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = kc.getGroup(op.param1)                                   
                                            G.preventedJoinByTicket = False
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.updateGroup(G)
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kc.getGroup(op.param1)                                                                     
                                            G.preventedJoinByTicket = True
                                            kc.updateGroup(G)
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kf.kickoutFromGroup(op.param1,[op.param2])
                                                kf.inviteIntoGroup(op.param1,[op.param3])
                                                kf.cancelGroupInvitation(op.param1,[op.param2]) #                                           
                                                kc.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                                    cl.cancelGroupInvitation(op.param1,[op.param2]) #                                              
                                                    kc.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                                        ki.cancelGroupInvitation(op.param1,[op.param2]) #                                                   
                                                        kc.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                                            kk.cancelGroupInvitation(op.param1,[op.param2]) #                                                      
                                                            kc.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kb.inviteIntoGroup(op.param1,[op.param3])
                        kb.cancelGroupInvitation(op.param1,[op.param2]) #              
                        kb.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ke.kickoutFromGroup(op.param1,[op.param2])
                            ke.inviteIntoGroup(op.param1,[op.param3])
                            ke.cancelGroupInvitation(op.param1,[op.param2]) #                        
                            kb.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kf.kickoutFromGroup(op.param1,[op.param2])
                                kf.inviteIntoGroup(op.param1,[op.param3])
                                kf.cancelGroupInvitation(op.param1,[op.param2]) #                 
                                kb.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                    ki.cancelGroupInvitation(op.param1,[op.param2]) #                           
                                    kb.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kj.kickoutFromGroup(op.param1,[op.param2])
                                        kj.inviteIntoGroup(op.param1,[op.param3])
                                        kj.cancelGroupInvitation(op.param1,[op.param2])                                
                                        kb.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = kb.getGroup(op.param1)
                                            G.preventedJoinByTicket = False                                                       
                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                            kb.updateGroup(G)                                  
                                            Ticket = kb.reissueGroupTicket(op.param1)                                     
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kb.getGroup(op.param1)
                                            G.preventedJoinByTicket = True                            
                                            kb.updateGroup(G)
                                            Ticket = kb.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kf.kickoutFromGroup(op.param1,[op.param2])
                                                kf.inviteIntoGroup(op.param1,[op.param3])
                                                kf.cancelGroupInvitation(op.param1,[op.param2]) #                                          
                                                kb.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                                    ki.cancelGroupInvitation(op.param1,[op.param2]) #                                       
                                                    kb.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                                        kk.cancelGroupInvitation(op.param1,[op.param2]) #                                                 
                                                        kb.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                                            kc.cancelGroupInvitation(op.param1,[op.param2]) #                                                  
                                                            kb.acceptGroupInvitation(op.param1)    
                                                        except:
                                                        	pass
                return

            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        ke.inviteIntoGroup(op.param1,[op.param3])
                        ke.cancelGroupInvitation(op.param1,[op.param2]) #                    
                        kd.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ke.kickoutFromGroup(op.param1,[op.param2])
                            ke.inviteIntoGroup(op.param1,[op.param3])
                            ke.cancelGroupInvitation(op.param1,[op.param2])                    
                            kd.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kf.kickoutFromGroup(op.param1,[op.param2])
                                kf.inviteIntoGroup(op.param1,[op.param3])
                                kf.cancelGroupInvitation(op.param1,[op.param2]) #                
                                kd.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                    ki.cancelGroupInvitation(op.param1,[op.param2]) #                                 
                                    kd.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                        kb.cancelGroupInvitation(op.param1,[op.param2]) #                                
                                        kd.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = kd.getGroup(op.param1)
                                            G.preventedJoinByTicket = False                                  
                                            G.preventedJoinByTicket = False
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.updateGroup(G)      
                                            Ticket = kd.reissueGroupTicket(op.param1)                                       
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kd.getGroup(op.param1)
                                            G.preventedJoinByTicket = True                              
                                            G.preventedJoinByTicket = True
                                            kd.updateGroup(G)
                                            Ticket = kd.reissueGroupTicket(op.param1)                                                             
                                        except:
                                            try:
                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                ki.cancelGroupInvitation(op.param1,[op.param2]) #          
                                                kd.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                                    kk.cancelGroupInvitation(op.param1,[op.param2]) #                                            
                                                    kd.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                        kc.cancelGroupInvitation(op.param1,[op.param2]) #                                                    
                                                        kd.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                                            kb.cancelGroupInvitation(op.param1,[op.param2]) #                                                  
                                                            kd.acceptGroupInvitation(op.param1)    
                                                        except:
                                                        	pass
                return

            if Fmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        ke.inviteIntoGroup(op.param1,[op.param3])
                        ke.cancelGroupInvitation(op.param1,[op.param2]) #                      
                        ke.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            kk.cancelGroupInvitation(op.param1,[op.param2]) #                          
                            ke.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                kc.cancelGroupInvitation(op.param1,[op.param2]) #                              
                                ke.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                    kd.cancelGroupInvitation(op.param1,[op.param2]) #                               
                                    ke.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                        kb.cancelGroupInvitation(op.param1,[op.param2]) #                                      
                                        ke.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = ke.getGroup(op.param1)
                                            G.preventedJoinByTicket = False                     
                                            G.preventedJoinByTicket = False
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.updateGroup(G)
                                            Ticket = ke.reissueGroupTicket(op.param1)                        
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = ke.getGroup(op.param1)                                        
                                            G.preventedJoinByTicket = True            
                                            ke.updateGroup(G)
                                            Ticket = ke.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kk.kickoutFromGroup(op.param1,[op.param2])
                                                kk.inviteIntoGroup(op.param1,[op.param3])
                                                kk.cancelGroupInvitation(op.param1,[op.param2])                                           
                                                ke.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                                    kc.cancelGroupInvitation(op.param1,[op.param2]) #                                              
                                                    ke.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                                        kb.cancelGroupInvitation(op.param1,[op.param2]) #                                                 
                                                        ke.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                                            kd.inviteIntoGroup(op.param1,[op.param3])
                                                            kd.cancelGroupInvitation(op.param1,[op.param2]) #                                                                                                         
                                                            ke.acceptGroupInvitation(op.param1)    
                                                        except:
                                                        	pass
                return

            if Gmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kf.kickoutFromGroup(op.param1,[op.param2])
                        kf.inviteIntoGroup(op.param1,[op.param3])
                        kf.cancelGroupInvitation(op.param1,[op.param2]) #  
                        kf.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kd.kickoutFromGroup(op.param1,[op.param2])
                            kd.inviteIntoGroup(op.param1,[op.param3])
                            kd.cancelGroupInvitation(op.param1,[op.param2]) #                       
                            kf.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ke.kickoutFromGroup(op.param1,[op.param2])
                                ke.inviteIntoGroup(op.param1,[op.param3])
                                ke.cancelGroupInvitation(op.param1,[op.param2])                          
                                kf.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                    ki.cancelGroupInvitation(op.param1,[op.param2]) #                                  
                                    kf.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        kk.cancelGroupInvitation(op.param1,[op.param2]) #                               
                                        kf.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = kf.getGroup(op.param1)
                                            G.preventedJoinByTicket = False                   
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                            kf.updateGroup(G)                                                      
                                            Ticket = kf.reissueGroupTicket(op.param1)                                 
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kf.getGroup(op.param1)
                                            G.preventedJoinByTicket = True                                  
                                            kf.updateGroup(G)
                                            Ticket = kf.reissueGroupTicket(op.param1)                 
                                        except:
                                            try:
                                                kb.kickoutFromGroup(op.param1,[op.param2])
                                                kb.inviteIntoGroup(op.param1,[op.param3])
                                                kb.cancelGroupInvitation(op.param1,[op.param2]) #                                             
                                                kf.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                                    kd.cancelGroupInvitation(op.param1,[op.param2]) #                                                  
                                                    kf.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                                        ki.cancelGroupInvitation(op.param1,[op.param2]) #                                                   
                                                        kf.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                                            kb.cancelGroupInvitation(op.param1,[op.param2]) #                                   
                                                            kf.acceptGroupInvitation(op.param1)    
                                                        except:
                                                        	pass                         
                return

            if Cmid in op.param3: #
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kc.cancelGroupInvitation(op.param1,[op.param2])                   
                        kj.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                            kb.cancelGroupInvitation(op.param1,[op.param2]) #                 
                            kj.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                ki.cancelGroupInvitation(op.param1,[op.param2]) #                   
                                kj.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                    kk.cancelGroupInvitation(op.param1,[op.param2]) #                                
                                    kj.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                        kd.cancelGroupInvitation(op.param1,[op.param2]) #                                 
                                        kj.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = kj.getGroup(op.param1)
                                            G.preventedJoinByTicket = False           
                                            kj.kickoutFromGroup(op.param1,[op.param2])
                                            kj.updateGroup(G)             
                                            Ticket = kj.reissueGroupTicket(op.param1)                                
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)                             
                                            G = kj.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            G = kd.getGroup(op.param1)                                    
                                            G.preventedJoinByTicket = True
                                            kj.updateGroup(G)
                                            Ticket = kj.reissueGroupTicket(op.param1)                                
                                        except:
                                            try:
                                                kd.kickoutFromGroup(op.param1,[op.param2])
                                                kd.inviteIntoGroup(op.param1,[op.param3])
                                                kd.cancelGroupInvitation(op.param1,[op.param2]) #                   
                                                kj.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                                    kb.cancelGroupInvitation(op.param1,[op.param2]) #                             
                                                    kj.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                                        ki.cancelGroupInvitation(op.param1,[op.param2]) #                                                     
                                                        kj.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                                            kk.cancelGroupInvitation(op.param1,[op.param2]) #                                                   
                                                            kj.acceptGroupInvitation(op.param1)    
                                                        except:
                                                        	pass
                return

            if Emid in op.param3: 
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        kd.inviteIntoGroup(op.param1,[op.param3])
                        kd.cancelGroupInvitation(op.param1,[op.param2]) #   
                        kd.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            ki.cancelGroupInvitation(op.param1,[op.param2]) #                        
                            kd.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                kk.cancelGroupInvitation(op.param1,[op.param2]) #                            
                                kd.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    kc.cancelGroupInvitation(op.param1,[op.param2]) #                               
                                    kd.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                        kb.cancelGroupInvitation(op.param1,[op.param2])                                    
                                        kd.acceptGroupInvitation(op.param1)     
                                    except:
                                        try:
                                            G = kd.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.updateGroup(G)
                                            Ticket = kd.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)                            
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = sw.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            sw.updateGroup(G)
                                            Ticket = sw.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kd.kickoutFromGroup(op.param1,[op.param2])
                                                kd.inviteIntoGroup(op.param1,[op.param3])
                                                kd.cancelGroupInvitation(op.param1,[op.param2])                                            
                                                kd.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                                    ki.cancelGroupInvitation(op.param1,[op.param2]) #                                    
                                                    kd.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                                        kk.cancelGroupInvitation(op.param1,[op.param2]) #              
                                                        kd.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                                            kc.cancelGroupInvitation(op.param1,[op.param2]) #
                                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                                            kd.acceptGroupInvitation(op.param1)    
                                                        except:
                                                            pass
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.cancelGroupInvitation(op.param1,[op.param2]) #
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.findAndAddContactsByMid(op.param3) # gipro
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.cancelGroupInvitation(op.param1,[op.param2]) #
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.findAndAddContactsByMid(op.param3) # gipro
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.cancelGroupInvitation(op.param1,[op.param2]) #
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.findAndAddContactsByMid(op.param3) # gipro
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.cancelGroupInvitation(op.param1,[op.param2]) #
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.findAndAddContactsByMid(op.param3) # gipro
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.cancelGroupInvitation(op.param1,[op.param2]) #
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.findAndAddContactsByMid(op.param3) # gipro
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.cancelGroupInvitation(op.param1,[op.param2]) #
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.findAndAddContactsByMid(op.param3) # gipro
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                            try:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                ke.cancelGroupInvitation(op.param1,[op.param2]) #
                                                ke.findAndAddContactsByMid(op.param1,admin)
                                                ke.findAndAddContactsByMid(op.param3) # gipro
                                                ke.inviteIntoGroup(op.param1,admin)
                                            except:
                                                try:
                                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                                    kf.cancelGroupInvitation(op.param1,[op.param2]) #
                                                    kf.findAndAddContactsByMid(op.param1,admin)
                                                    kf.findAndAddContactsByMid(op.param3) # gipro
                                                    kf.inviteIntoGroup(op.param1,admin)
                                                except:
                                                    try:
                                                        kj.kickoutFromGroup(op.param1,[op.param2])
                                                        kj.cancelGroupInvitation(op.param1,[op.param2]) #
                                                        kj.findAndAddContactsByMid(op.param1,admin)
                                                        kj.findAndAddContactsByMid(op.param3) # gipro
                                                        kj.inviteIntoGroup(op.param1,admin)  
                                                    except:
                                                        try:
                                                            sw.kickoutFromGroup(op.param1,[op.param2])
                                                            sw.cancelGroupInvitation(op.param1,[op.param2]) #
                                                            sw.findAndAddContactsByMid(op.param1,admin)
                                                            sw.findAndAddContactsByMid(op.param3) # gipro
                                                            sw.inviteIntoGroup(op.param1,admin)  
                                                        except:
                                                            pass

                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.cancelGroupInvitation(op.param1,[op.param2]) #
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.findAndAddContactsByMid(op.param3) #gipro
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.cancelGroupInvitation(op.param1,[op.param2]) #
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.findAndAddContactsByMid(op.param3) # gipro
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.cancelGroupInvitation(op.param1,[op.param2]) #
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.findAndAddContactsByMid(op.param3) # gipro
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.cancelGroupInvitation(op.param1,[op.param2]) #
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.findAndAddContactsByMid(op.param3) # gipro
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.cancelGroupInvitation(op.param1,[op.param2]) #
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.findAndAddContactsByMid(op.param3) # gipro
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.cancelGroupInvitation(op.param1,[op.param2]) #
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.findAndAddContactsByMid(op.param3) # gipro
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                            try:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                ke.cancelGroupInvitation(op.param1,[op.param2]) #
                                                ke.findAndAddContactsByMid(op.param1,admin)
                                                ke.findAndAddContactsByMid(op.param3) # gipro
                                                ke.inviteIntoGroup(op.param1,admin)
                                            except:
                                                 try:
                                                     kf.kickoutFromGroup(op.param1,[op.param2])
                                                     kf.cancelGroupInvitation(op.param1,[op.param2]) #
                                                     kf.findAndAddContactsByMid(op.param1,admin)
                                                     kf.findAndAddContactsByMid(op.param3) # gipro
                                                     kf.inviteIntoGroup(op.param1,admin)
                                                 except:
                                                     try:
                                                         kj.kickoutFromGroup(op.param1,[op.param2])
                                                         kj.cancelGroupInvitation(op.param1,[op.param2]) #
                                                         kj.findAndAddContactsByMid(op.param1,admin)
                                                         kj.findAndAddContactsByMid(op.param3) # gipro
                                                         kj.inviteIntoGroup(op.param1,admin)  
                                                     except:
                                                        try:
                                                            sw.kickoutFromGroup(op.param1,[op.param2])
                                                            sw.cancelGroupInvitation(op.param1,[op.param2]) #
                                                            sw.findAndAddContactsByMid(op.param1,admin)
                                                            sw.findAndAddContactsByMid(op.param3) # gipro
                                                            sw.inviteIntoGroup(op.param1,admin)  
                                                        except:
                                                            pass
                                                           
            
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.cancelGroupInvitation(op.param1,[op.param2]) #
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.findAndAddContactsByMid(op.param3) # gipro
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.cancelGroupInvitation(op.param1,[op.param2]) #
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.findAndAddContactsByMid(op.param3) # gipro
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.cancelGroupInvitation(op.param1,[op.param2]) #
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.findAndAddContactsByMid(op.param3) # gipro
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.cancelGroupInvitation(op.param1,[op.param2]) #
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.findAndAddContactsByMid(op.param3) # gipro
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.cancelGroupInvitation(op.param1,[op.param2]) #
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.findAndAddContactsByMid(op.param3) # gipro
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.cancelGroupInvitation(op.param1,[op.param2]) #
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.findAndAddContactsByMid(op.param3) # gipro
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.cancelGroupInvitation(op.param1,[op.param2]) #
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.findAndAddContactsByMid(op.param3) # gipro
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.cancelGroupInvitation(op.param1,[op.param2]) #
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.findAndAddContactsByMid(op.param3) # gipro
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       kj.kickoutFromGroup(op.param1,[op.param2])
                                                       kj.cancelGroupInvitation(op.param1,[op.param2]) #
                                                       kj.findAndAddContactsByMid(op.param1,admin)
                                                       kj.findAndAddContactsByMid(op.param3) # gipro
                                                       kj.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           sw.kickoutFromGroup(op.param1,[op.param2])
                                                           sw.cancelGroupInvitation(op.param1,[op.param2]) #
                                                           sw.findAndAddContactsByMid(op.param1,admin)
                                                           sw.findAndAddContactsByMid(op.param3) # gipro
                                                           sw.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass          

                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.cancelGroupInvitation(op.param1,[op.param2]) #
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.findAndAddContactsByMid(op.param3) # gipro
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.cancelGroupInvitation(op.param1,[op.param2]) #
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.findAndAddContactsByMid(op.param3) # gipro
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.cancelGroupInvitation(op.param1,[op.param2]) #
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.findAndAddContactsByMid(op.param3) # gipro
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.cancelGroupInvitation(op.param1,[op.param2]) #
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.findAndAddContactsByMid(op.param3) # gipro
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.cancelGroupInvitation(op.param1,[op.param2]) #
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.findAndAddContactsByMid(op.param3) # gipro
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.cancelGroupInvitation(op.param1,[op.param2]) #
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.findAndAddContactsByMid(op.param3) # gipro
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.cancelGroupInvitation(op.param1,[op.param2]) #
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.findAndAddContactsByMid(op.param3) # gipro
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.cancelGroupInvitation(op.param1,[op.param2]) #
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.findAndAddContactsByMid(op.param3) # gipro
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       kj.kickoutFromGroup(op.param1,[op.param2])
                                                       kj.cancelGroupInvitation(op.param1,[op.param2]) #
                                                       kj.findAndAddContactsByMid(op.param1,admin)
                                                       kj.findAndAddContactsByMid(op.param3) # gipro
                                                       kj.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           sw.kickoutFromGroup(op.param1,[op.param2])
                                                           sw.cancelGroupInvitation(op.param1,[op.param2]) #
                                                           sw.findAndAddContactsByMid(op.param1,admin)
                                                           sw.findAndAddContactsByMid(op.param3) # gipro
                                                           sw.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass
                                                           
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.cancelGroupInvitation(op.param1,[op.param2]) #
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.findAndAddContactsByMid(op.param3) # gipro
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.cancelGroupInvitation(op.param1,[op.param2]) #
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.findAndAddContactsByMid(op.param3) # gipro
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.cancelGroupInvitation(op.param1,[op.param2]) #
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.findAndAddContactsByMid(op.param3) # gipro
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.cancelGroupInvitation(op.param1,[op.param2]) #
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.findAndAddContactsByMid(op.param3) # gipro
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.cancelGroupInvitation(op.param1,[op.param2]) #
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.findAndAddContactsByMid(op.param3) # gipro
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.cancelGroupInvitation(op.param1,[op.param2]) #
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.findAndAddContactsByMid(op.param3) # gipro
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.cancelGroupInvitation(op.param1,[op.param2]) #
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.findAndAddContactsByMid(op.param3) # gipro
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.cancelGroupInvitation(op.param1,[op.param2]) #
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.findAndAddContactsByMid(op.param3) # gipro
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       kj.kickoutFromGroup(op.param1,[op.param2])
                                                       kj.cancelGroupInvitation(op.param1,[op.param2]) #
                                                       kj.findAndAddContactsByMid(op.param1,admin)
                                                       kj.findAndAddContactsByMid(op.param3) # gipro
                                                       kj.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           sw.kickoutFromGroup(op.param1,[op.param2])
                                                           sw.cancelGroupInvitation(op.param1,[op.param2]) #
                                                           sw.findAndAddContactsByMid(op.param1,admin)
                                                           sw.findAndAddContactsByMid(op.param3) # gipro
                                                           sw.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass       
                                                           
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.cancelGroupInvitation(op.param1,[op.param2]) #
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.findAndAddContactsByMid(op.param3) # gipro
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.cancelGroupInvitation(op.param1,[op.param2]) #
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.findAndAddContactsByMid(op.param3) # gipro
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.cancelGroupInvitation(op.param1,[op.param2]) #
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.findAndAddContactsByMid(op.param3) # gipro
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.cancelGroupInvitation(op.param1,[op.param2]) #
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.findAndAddContactsByMid(op.param3) # gipro
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.cancelGroupInvitation(op.param1,[op.param2]) #
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.findAndAddContactsByMid(op.param3) # gipro
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.cancelGroupInvitation(op.param1,[op.param2]) #
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.findAndAddContactsByMid(op.param3) # gipro
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.cancelGroupInvitation(op.param1,[op.param2]) #
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.findAndAddContactsByMid(op.param3) # gipro
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.cancelGroupInvitation(op.param1,[op.param2]) #
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.findAndAddContactsByMid(op.param3) # gipro
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       kj.kickoutFromGroup(op.param1,[op.param2])
                                                       kj.cancelGroupInvitation(op.param1,[op.param2]) #
                                                       kj.findAndAddContactsByMid(op.param1,admin)
                                                       kj.findAndAddContactsByMid(op.param3) # gipro
                                                       kj.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           sw.kickoutFromGroup(op.param1,[op.param2])
                                                           sw.cancelGroupInvitation(op.param1,[op.param2]) #
                                                           sw.findAndAddContactsByMid(op.param1,admin)
                                                           sw.findAndAddContactsByMid(op.param3) # gipro
                                                           sw.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass         

                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.cancelGroupInvitation(op.param1,[op.param2]) #
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.findAndAddContactsByMid(op.param3) # gipro
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.cancelGroupInvitation(op.param1,[op.param2]) #
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.findAndAddContactsByMid(op.param3) # gipro
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.cancelGroupInvitation(op.param1,[op.param2]) #
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.findAndAddContactsByMid(op.param3) # gipro
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.cancelGroupInvitation(op.param1,[op.param2]) #
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.findAndAddContactsByMid(op.param3) # gipro
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.cancelGroupInvitation(op.param1,[op.param2]) #
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.findAndAddContactsByMid(op.param3) # gipro
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.cancelGroupInvitation(op.param1,[op.param2]) #
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.findAndAddContactsByMid(op.param3) # gipro
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.cancelGroupInvitation(op.param1,[op.param2]) #
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.findAndAddContactsByMid(op.param3) # gipro
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.cancelGroupInvitation(op.param1,[op.param2]) #
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.findAndAddContactsByMid(op.param3) # gipro
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       kj.kickoutFromGroup(op.param1,[op.param2])
                                                       kj.cancelGroupInvitation(op.param1,[op.param2]) #
                                                       kj.findAndAddContactsByMid(op.param1,admin)
                                                       kj.findAndAddContactsByMid(op.param3) # gipro
                                                       kj.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           sw.kickoutFromGroup(op.param1,[op.param2])
                                                           sw.cancelGroupInvitation(op.param1,[op.param2]) #
                                                           sw.findAndAddContactsByMid(op.param1,admin)
                                                           sw.findAndAddContactsByMid(op.param3) # gipro
                                                           sw.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass
                                                           
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.cancelGroupInvitation(op.param1,[op.param2]) #
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.findAndAddContactsByMid(op.param3) # gipro
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.cancelGroupInvitation(op.param1,[op.param2]) #
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.findAndAddContactsByMid(op.param3) # gipro
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.cancelGroupInvitation(op.param1,[op.param2]) #
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.findAndAddContactsByMid(op.param3) # gipro
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.cancelGroupInvitation(op.param1,[op.param2]) #
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.findAndAddContactsByMid(op.param3) # gipro
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.cancelGroupInvitation(op.param1,[op.param2]) #
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.findAndAddContactsByMid(op.param3) # gipro
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.cancelGroupInvitation(op.param1,[op.param2]) #
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.findAndAddContactsByMid(op.param3) # gipro
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.cancelGroupInvitation(op.param1,[op.param2]) #
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.findAndAddContactsByMid(op.param3) # gipro
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.cancelGroupInvitation(op.param1,[op.param2]) #
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.findAndAddContactsByMid(op.param3) # gipro
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       kj.kickoutFromGroup(op.param1,[op.param2])
                                                       kj.cancelGroupInvitation(op.param1,[op.param2]) #
                                                       kj.findAndAddContactsByMid(op.param1,admin)
                                                       kj.findAndAddContactsByMid(op.param3) # gipro
                                                       kj.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           sw.kickoutFromGroup(op.param1,[op.param2])
                                                           sw.cancelGroupInvitation(op.param1,[op.param2]) #
                                                           sw.findAndAddContactsByMid(op.param1,admin)
                                                           sw.findAndAddContactsByMid(op.param3) # gipro
                                                           sw.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass          

                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.cancelGroupInvitation(op.param1,[op.param2]) #
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.findAndAddContactsByMid(op.param3) # gipro
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.cancelGroupInvitation(op.param1,[op.param2]) #
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.findAndAddContactsByMid(op.param3) # gipro
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.cancelGroupInvitation(op.param1,[op.param2]) #
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.findAndAddContactsByMid(op.param3) # gipro
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.cancelGroupInvitation(op.param1,[op.param2]) #
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.findAndAddContactsByMid(op.param3) # gipro
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.cancelGroupInvitation(op.param1,[op.param2]) #
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.findAndAddContactsByMid(op.param3) # gipro
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.cancelGroupInvitation(op.param1,[op.param2]) #
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.findAndAddContactsByMid(op.param3) # gipro
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.cancelGroupInvitation(op.param1,[op.param2]) #
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.findAndAddContactsByMid(op.param3) # gipro
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.cancelGroupInvitation(op.param1,[op.param2]) #
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.findAndAddContactsByMid(op.param3) # gipro
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       kj.kickoutFromGroup(op.param1,[op.param2])
                                                       kj.cancelGroupInvitation(op.param1,[op.param2]) #
                                                       kj.findAndAddContactsByMid(op.param1,admin)
                                                       kj.findAndAddContactsByMid(op.param3) # gipro
                                                       kj.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           sw.kickoutFromGroup(op.param1,[op.param2])
                                                           sw.cancelGroupInvitation(op.param1,[op.param2]) #
                                                           sw.findAndAddContactsByMid(op.param1,admin)
                                                           sw.findAndAddContactsByMid(op.param3) # gipro
                                                           sw.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass          

                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.cancelGroupInvitation(op.param1,[op.param2]) #
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.findAndAddContactsByMid(op.param3) # gipro
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.cancelGroupInvitation(op.param1,[op.param2]) #
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.findAndAddContactsByMid(op.param3) # gipro
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.cancelGroupInvitation(op.param1,[op.param2]) #
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.findAndAddContactsByMid(op.param3) # gipro
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.cancelGroupInvitation(op.param1,[op.param2]) #
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.findAndAddContactsByMid(op.param3) # gipro
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.cancelGroupInvitation(op.param1,[op.param2]) #
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.findAndAddContactsByMid(op.param3) # gipro
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.cancelGroupInvitation(op.param1,[op.param2]) #
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.findAndAddContactsByMid(op.param3) # gipro
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.cancelGroupInvitation(op.param1,[op.param2]) #
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.findAndAddContactsByMid(op.param3) # gipro
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.cancelGroupInvitation(op.param1,[op.param2]) #
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.findAndAddContactsByMid(op.param3) # gipro
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       kj.kickoutFromGroup(op.param1,[op.param2])
                                                       kj.cancelGroupInvitation(op.param1,[op.param2]) #
                                                       kj.findAndAddContactsByMid(op.param1,admin)
                                                       kj.findAndAddContactsByMid(op.param3) # gipro
                                                       kj.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           sw.kickoutFromGroup(op.param1,[op.param2])
                                                           sw.cancelGroupInvitation(op.param1,[op.param2]) #
                                                           sw.findAndAddContactsByMid(op.param1,admin)
                                                           sw.findAndAddContactsByMid(op.param3) # gipro
                                                           sw.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass
                                                           
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.cancelGroupInvitation(op.param1,[op.param2]) #
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.findAndAddContactsByMid(op.param3) # gipro
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.cancelGroupInvitation(op.param1,[op.param2]) #
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.findAndAddContactsByMid(op.param3) # gipro
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.cancelGroupInvitation(op.param1,[op.param2]) #
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.findAndAddContactsByMid(op.param3) # gipro
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.cancelGroupInvitation(op.param1,[op.param2]) #
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.findAndAddContactsByMid(op.param3) # gipro
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.cancelGroupInvitation(op.param1,[op.param2]) #
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.findAndAddContactsByMid(op.param3) # gipro
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.cancelGroupInvitation(op.param1,[op.param2]) #
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.findAndAddContactsByMid(op.param3) # gipro
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.cancelGroupInvitation(op.param1,[op.param2]) #
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.findAndAddContactsByMid(op.param3) # gipro
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.cancelGroupInvitation(op.param1,[op.param2]) #
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.findAndAddContactsByMid(op.param3) # gipro
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       kj.kickoutFromGroup(op.param1,[op.param2])
                                                       kj.cancelGroupInvitation(op.param1,[op.param2]) #
                                                       kj.findAndAddContactsByMid(op.param1,admin)
                                                       kj.findAndAddContactsByMid(op.param3) # gipro
                                                       kj.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           sw.kickoutFromGroup(op.param1,[op.param2])
                                                           sw.cancelGroupInvitation(op.param1,[op.param2]) #
                                                           sw.findAndAddContactsByMid(op.param1,admin)
                                                           sw.findAndAddContactsByMid(op.param3) # gipro
                                                           sw.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass           
                                
                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["RAreadPoint"]:
                   if op.param2 in Setmain["RAreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["RAreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 5:
            print ("[ 5 ] NOTIFIED AUTO BLOCK CONTACT")
            if wait["autoBlock"] == True:
                cl.blockContact(op.param1)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 ɢᴀᴍʙᴀʀ ᴅɪʜᴀᴘᴜs  」\n• ✅ ➡ᴘᴇɴɢɪʀɪᴍ : "
                                ret_ = "• ✅ ➡ɴᴀᴍᴀ ɢʀᴜᴘ: {}".format(str(ginfo.name))
                                ret_ += "\n• ✅ ➡ᴡᴀᴋᴛᴜ ɴɢɪʀɪᴍ : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n✅✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺"
                                ret_ += "\n✅Creator:  line.me/ti/p/~kaway27" 
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 ᴘᴇsᴀɴ ᴅɪʜᴀᴘᴜs  」\n"
                                ret_ += "• ↪➣ ᴘᴇɴɢɪʀɪᴍ : {}".format(str(ryan.displayName))
                                ret_ += "\n• ↪➣ ɴᴀᴍᴀ ɢʀᴜᴘ : {}".format(str(ginfo.name))
                                ret_ += "\n• ↪➣ ᴡᴀᴋᴛᴜ ɴɢɪʀɪᴍ: {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• ↪➣ᴘᴇsᴀɴɴʏᴀ : {}".format(str(msg_dict[msg_id]["text"]))
                                ret_ += "\n🔳✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺"
                                ret_ += "\n🔳Creator:  line.me/ti/p/~kaway27" 
                                cl.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 sᴛɪᴄᴋᴇʀ ᴅɪʜᴀᴘᴜs」\n"
                                ret_ += "• 🌠 ᴘᴇɴɢɪʀɪᴍ : {}".format(str(ryan.displayName))
                                ret_ += "\n• 🌠 ɴᴀᴍᴀ ɢʀᴜᴘ : {}".format(str(ginfo.name))
                                ret_ += "\n• 🌠 ᴡᴀᴋᴛᴜ ɴɢɪʀɪᴍ : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "\n🔀✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺"
                                ret_ += "\n🔀Creator:  line.me/ti/p/~kaway27" 
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 55:
            try:
                if op.param1 in Setmain["ARreadPoint"]:
                   if op.param2 in Setmain["ARreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["ARreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        sider = cl.getContact(op.param2).picturePath
                        image = 'http://dl.profile.line.naver.jp'+sider
                        cl.sendImageWithURL(op.param1, image)

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                   if msg._from in wait["blacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   contact = cl.getContact(msg._from)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           saints = cl.getContact(msg._from)
                           sendMention(msg.to, saints.mid, "", wait["Respontag"])
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"25628787","STKPKGID":"1818607","STKVER":"1"}, contentType=7)
                           cl.sendMessage(msg.to, wait["Respontag"])
                           cl.sendImageWithURL(msg.to,image)
                           rnd = ["yg nge tag semoga dapet tikungan amin"]
                           p = random.choice(rnd)
                           lang = 'id'
                           tts = gTTS(text=p, lang=lang)
                           tts.save("hasil.mp3")
                           cl.sendAudio(msg.to,"hasil.mp3")
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"25628787","STKPKGID":"1818607","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in admin:
                           saints = cl.getContact(msg._from)
                           sendMention(msg.to, saints.mid, "", wait["Respontag"])
                           cl.sendMessage(msg.to, None, contentMetadata={"PRDID":"a0768339-c2d3-4189-9653-2909e9bb6f58","PRDTYPE":"THEME","MSGTPL":"6"}, contentType=9)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["mentionKick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in admin:
                           cl.sendMessage(msg.to, "Ngetag lagi\nCipok nich")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
#SPAMINVITE
               if op.type == 25:
                 if settings['SpamInvite'] == True:
                   msg = op.message
                   man = msg._from
                   send = msg.to
                   if msg.contentType == 13:
                       if msg._from in admin:
                           korban = msg.contentMetadata["displayName"]
                           invite = msg.contentMetadata["mid"]
                           groups = client.getGroup(send)
                           pending = groups.invitee
                           targets = []
                           for x in groups.members:
                               if korban in x.displayName:
                                   client.sendText(send, korban + " Sudah Berada DiGrup Ini")
                               else:
                                   targets.append(invite)
                           if targets == []:
                               pass
                           else:
                               for target in targets:
                                   try:
                                       cl.findAndAddContactsByMid(target)
                                       cl.createGroup("KAMU DISPAM DUDUL",[target]) 
                                       cl.createGroup("KAMU DISPAM DUDUL",[target]) 
                                       cl.createGroup("KAMU DISPAM DUDUL",[target])
                                       cl.sendText(send,"Spam Invite ke " + korban + "\nSUCCESS..")
                                       settings['SpamInvite'] = False
                                   except:             
                                        cl.sendText(send, 'Contact error')
                                        settings['SpamInvite'] = False
                                        break
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
               if msg.toType == 0:
                    to = msg._from
               elif msg.toType == 2:
                    to = msg.to
               if msg.contentType == 16:
                    if wait["Timeline"] == True:
                            ret_ = "「 ᴅᴇᴛᴀɪʟ ᴘᴏsᴛɪɴɢᴀɴ 」"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = cl.getContact(sender)
                                auth = "\n•  🎞༎  ▶ᴘᴇɴᴜʟɪs : {}".format(str(contact.displayName))
                            else:
                                auth = "\n•  🎞༎  ▶ᴘᴇɴᴜʟɪs : {}".format(str(msg.contentMetadata["serviceName"]))
                            ret_ += auth
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n•🎞༎  ▶sᴛɪᴄᴋᴇʀ : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n• 🎞༎  ▶ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n•🎞༎  ▶Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n• 🎞༎  ▶Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n•??༎  ▶Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                    ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n• 🎞༎  ▶Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n• 🎞༎  ▶Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "text" in msg.contentMetadata:
                                text = "\n• 🎞༎  ▶Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                purl = "\n• 🎞༎  ▶Post URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += purl
                                ret_ += text
                            cl.sendMessage(to, str(ret_))
                            cl.like(url[25:58], url[66:], likeType=1005)
                            cl.comment(url[25:58], url[66:], wait["message"])
               if msg.contentType == 0:
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 sᴛɪᴄᴋᴇʀ ɪɴғᴏ 」"
                   ret_ += "\n• 🔷༎  ➡sᴛɪᴄᴋᴇʀ ɪᴅ: {}".format(stk_id)
                   ret_ += "\n• 🔷༎  ➡sᴛɪᴄᴋᴇʀ ᴠᴇʀsɪᴏɴ : {}".format(stk_ver)
                   ret_ += "\n• 🔷༎  ➡sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋᴀɢᴇ : {}".format(pkg_id)
                   ret_ += "\n• 🔷༎  ➡sᴛɪᴄᴋᴇʀ ᴜʀʟ: line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                if wait["stickerOn"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        r = s.get("https://store.line.me/stickershop/product/{}/id".format(urllib.parse.quote(pkg_id)))
                        soup = BeautifulSoup(r.content, 'html5lib')
                        data = soup.select("[class~=mdBtn01Txt]")[0].text
                        if data == 'Lihat Produk Lain':
                            ret_ = "「 sᴛɪᴄᴋᴇʀ ɪɴғᴏ 」"
                            ret_ += "\n• ✳➣༎  ▶sᴛɪᴄᴋᴇʀ ɪᴅ : {}".format(stk_id)
                            ret_ += "\n• ✳➣༎  ▶sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋᴀɢᴇ : {}".format(pkg_id)
                            ret_ += "\n•✳➣༎  ▶  : {}".format(stk_ver)
                            ret_ += "\n• sᴛɪᴄᴋᴇʀ ᴜʀʟ : line://shop/detail/{}".format(pkg_id)
                            cl.sendMessage(msg.to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = cl.downloadFileURL(data)
                               cl.sendImage(msg.to,path)
                        else:
                            ret_ = "「 sᴛɪᴄᴋᴇʀ ɪɴғᴏ 」"
                            ret_ += "\n•🔯༎  ▶PRICE : "+soup.findAll('p', attrs={'class':'mdCMN08Price'})[0].text
                            ret_ += "\n•🔯༎  ▶AUTHOR : "+soup.select("a[href*=/stickershop/author]")[0].text
                            ret_ += "\n•🔯༎  ▶sᴛɪᴄᴋᴇʀ ɪᴅ : {}".format(str(stk_id))
                            ret_ += "\n•🔯༎  ▶sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋᴀɢᴇ : {}".format(str(pkg_id))
                            ret_ += "\n•🔯༎  ▶sᴛɪᴄᴋᴇʀ ᴠᴇʀsɪᴏɴ : {}".format(str(stk_ver))
                            ret_ += "\n•🔯༎  ▶sᴛɪᴄᴋᴇʀ ᴜʀʟ : line://shop/detail/{}".format(str(pkg_id))
                            ret_ += "\n•🔯༎  ▶DESCRIPTION :\n"+soup.findAll('p', attrs={'class':'mdCMN08Desc'})[0].text
                            cl.sendMessage(msg.to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = cl.downloadFileURL(data)
                               cl.sendImage(msg.to,path)
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to," 「 Contact Info 」\n「✭」 Nama : " + msg.contentMetadata["displayName"] + "\n「✭」 MID : " + msg.contentMetadata["mid"] + "\n「✭」 Status Msg : " + contact.statusMessage + "\n「✭」 Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
               if msg.contentType == 13:
                if msg._from in admin:
                  if wait["invite"] == True:
                    msg.contentType = 0
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in wait["blacklist"]:
                            cl.sendMessage(msg.to, "「Dia ke bl kak... hpus bl dulu lalu invite lagi」")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                             try:
                                  cl.findAndAddContactsByMid(target)
                                  cl.inviteIntoGroup(msg.to,[target])
                                  ryan = cl.getContact(target)
                                  zx = ""
                                  zxc = ""
                                  zx2 = []
                                  xpesan =  "「 Sukses Invite 」\nNama "
                                  ret_ = "「Ketik Invite off jika sudah done」"
                                  ry = str(ryan.displayName)
                                  pesan = ''
                                  pesan2 = pesan+"@x\n"
                                  xlen = str(len(zxc)+len(xpesan))
                                  xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                  zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                  zx2.append(zx)
                                  zxc += pesan2
                                  text = xpesan + zxc + ret_ + ""
                                  cl.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  wait["invite"] = False
                                  break
                             except:
                                  cl.sendText(msg.to,"Anda terkena limit")
                                  wait["invite"] = False
                                  break
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"ᴄᴏɴᴛᴀᴄᴛ sᴜᴅᴀʜ ᴊᴀᴅɪ ᴀɴɢɢᴏᴛᴀ ʙᴏᴛs")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴀᴍʙᴀʜ ᴀɴɢɢᴏᴛᴀ ʙᴏᴛs")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢʜᴀᴘᴜs ᴀɴɢɢᴏᴛᴀ ʙᴏᴛs")
                    else:
                        wait["dellbots"] = True
                        cl.sendMessage(msg.to,"ᴄᴏɴᴛᴀᴄᴛ ʙᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ʙᴏᴛs✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺ ")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if wait["Addimage"]["status"] == True:
                        path = cl.downloadObjectMsg(msg.id)
                        images[wait["Addimage"]["name"]] = str(path)
                        f = codecs.open("image.json","w","utf-8")
                        json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ɢᴀᴍʙᴀʀ {}".format(str(wait["Addimage"]["name"])))
                        wait["Addimage"]["status"] = False                
                        wait["Addimage"]["name"] = ""
               if msg.contentType == 2:
                 if msg._from in admin:
                    if wait["Addvideo"]["status"] == True:
                        path = cl.downloadObjectMsg(msg.id)
                        videos[wait["Addvideo"]["name"]] = str(path)
                        f = codecs.open("video.json","w","utf-8")
                        json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "Berhasil menambahkan video {}".format(str(wait["Addvideo"]["name"])))
                        wait["Addvideo"]["status"] = False                
                        wait["Addvideo"]["name"] = ""
               if msg.contentType == 7:
                 if msg._from in admin:
                    if wait["Addsticker"]["status"] == True:
                        stickers[wait["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                        f = codecs.open("sticker.json","w","utf-8")
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "Berhasil menambahkan sticker {}".format(str(wait["Addsticker"]["name"])))
                        wait["Addsticker"]["status"] = False                
                        wait["Addsticker"]["name"] = ""
               if msg.contentType == 3:
                 if msg._from in admin:
                    if wait["Addaudio"]["status"] == True:
                        path = cl.downloadObjectMsg(msg.id)
                        audios[wait["Addaudio"]["name"]] = str(path)
                        f = codecs.open("audio.json","w","utf-8")
                        json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "Berhasil menambahkan mp3 {}".format(str(wait["Addaudio"]["name"])))
                        wait["Addaudio"]["status"] = False                
                        wait["Addaudio"]["name"] = ""
               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["ARfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["ARfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["ARfoto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Bmid]
                            kk.updateProfilePicture(path)
                            kk.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["ARfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Cmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Dmid in Setmain["ARfoto"]:
                            path = kb.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Dmid]
                            kb.updateProfilePicture(path)
                            kb.sendMessage(msg.to,"Foto berhasil dirubah") 
                        elif Emid in Setmain["ARfoto"]:
                            path = kd.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Emid]
                            kd.updateProfilePicture(path)
                            kd.sendMessage(msg.to,"Foto berhasil dirubah")   
                        elif Fmid in Setmain["ARfoto"]:
                            path = ke.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Fmid]
                            ke.updateProfilePicture(path)
                            ke.sendMessage(msg.to,"Foto berhasil dirubah")     
                        elif Gmid in Setmain["ARfoto"]:
                            path = kf.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Gmid]
                            kf.updateProfilePicture(path)
                            kf.sendMessage(msg.to,"Foto berhasil dirubah")       
                        elif Hmid in Setmain["ARfoto"]:
                            path = kg.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Hmid]
                            kg.updateProfilePicture(path)
                            kg.sendMessage(msg.to,"Foto berhasil dirubah")        
                        elif Imid in Setmain["ARfoto"]:
                            path = kh.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Imid]
                            kh.updateProfilePicture(path)
                            kh.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Jmid in Setmain["ARfoto"]:
                            path = kh.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Jmid]
                            kj.updateProfilePicture(path)
                            kj.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Zmid in Setmain["ARfoto"]:
                            path = sw.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Zmid]
                            sw.updateProfilePicture(path)
                            sw.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     path2 = kk.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     path4 = kb.downloadObjectMsg(msg_id)
                     path5 = kd.downloadObjectMsg(msg_id)
                     path6 = ke.downloadObjectMsg(msg_id)
                     path7 = kf.downloadObjectMsg(msg_id)
                     path8 = kj.downloadObjectMsg(msg_id)
                     path9 = sw.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kk.updateProfilePicture(path2)
                     kk.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kb.updateProfilePicture(path3)
                     kb.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kd.updateProfilePicture(path3)
                     kd.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     ke.updateProfilePicture(path3)
                     ke.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kf.updateProfilePicture(path3)
                     kf.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kj.updateProfilePicture(path3)
                     kj.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     sw.updateProfilePicture(path3)
                     sw.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
               if msg.contentType == 2:
                   if msg._from in admin:
                       if mid in Setmain["ARvideo"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["ARvideo"][mid]
                            cl.updateProfileVideoPicture(path)
                            cl.sendMessage(msg.to,"Foto berhasil dirubah jadi video")

               if msg.contentType == 0:
                 if Setmain["autoRead"] == True:
                     cl.sendChatChecked(msg.to, msg_id)
                 if text is None:
                     return
                 else:
                        for sticker in stickers:
                         if msg._from in admin:
                           if text.lower() == sticker:
                              sid = stickers[text.lower()]["STKID"]
                              spkg = stickers[text.lower()]["STKPKGID"]
                              cl.sendSticker(to, spkg, sid)
                        for image in images:
                         if msg._from in admin:
                           if text.lower() == image:
                              cl.sendImage(msg.to, images[image])
                        for audio in audios:
                         if msg._from in admin:
                           if text.lower() == audio:
                              cl.sendAudio(msg.to, audios[audio])
                        for video in videos:
                         if msg._from in admin:
                           if text.lower() == video:
                              cl.sendVideo(msg.to, videos[video])
                        cmd = command(text)
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                cl.sendText(msg.to, "Selfbot diaktifkan")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                cl.sendText(msg.to, "Selfbot dinonaktifkan")
                                            
                        elif cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                helpMessage = help()
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「My Name 'S」\n• User : "
                                ret_ = str(helpMessage)
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "help1":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                helpMessage1 = help1()
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「MY Name 'S」\n• User : "
                                ret_ = str(helpMessage1)
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                helpMessage2 = help2()
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「MY Nme 'S」\n• User : "
                                ret_ = str(helpMessage2)
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "help3":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                helpMessage3 = help3()
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「MY Name 'S」\n• User : "
                                ret_ = str(helpMessage3)
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "\n       「↪✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺↩」\n"
                                if wait["stickerOn"] == True: md+="「🔲」 Sticker「ON」📲\n"
                                else: md+="「🔲」 Sticker「OFF」📵\n"
                                if wait["contact"] == True: md+="「🔲」 Contact「ON」📲\n"
                                else: md+="「🔲」 Contact「OFF」📵\n"
                                if wait["talkban"] == True: md+="「🔲」 Talkban「ON」📲\n"
                                else: md+="「🔲」 Talkban「OFF」??\n"
                                if wait["unsend"] == True: md+="「🔲」 Unsend「ON」📲\n"
                                else: md+="「🔲」 Unsend「OFF」📵\n"
                                if settings["SpamInvite"] == True: md+="「🔲」 Spaminvite「ON」📲\n"
                                else: md+="「🔲」 Spaminvite「OFF」📵\n"
                                if wait["detectMention"] == True: md+="「🔲」 Respon「ON」📲\n"
                                else: md+="「🔲」 Respon「OFF」📵\n"
                                if wait["Timeline"] == True: md+="「🔲」 Timeline「ON」📲\n"
                                else: md+="「🔲」 Timeline「OFF」📵\n"
                                if wait["autoJoin"] == True: md+="「🔲」 Autojoin「ON」📲\n"
                                else: md+="「🔲」 Autojoin「OFF」📵\n"
                                if wait["autoAdd"] == True: md+="「🔲」 Autoadd「ON」📲\n"
                                else: md+="「🔲」 Autoadd「OFF」📵\n"
                                if settings["autoJoinTicket"] == True: md+="「✭」 Jointicket「ON」📲\n"
                                else: md+="「🔲」 Jointicket「OFF」📵\n"
                                if msg.to in welcome: md+="「🔲」 Welcome「ON」📲\n"
                                else: md+="「🔲」 Welcome「OFF」📵\n"
                                if wait["autoLeave"] == True: md+="「🔲」 Autoleave「ON」📲\n"
                                else: md+="「🔲」 Autoleave「OFF」📵\n"
                                if msg.to in protectqr: md+="「🔲」Protecturl「ON」📲\n"
                                else: md+="「🔲」Protecturl「OFF」📵\n"
                                if msg.to in protectjoin: md+="「🔲」Protectjoin「ON」📲\n"
                                else: md+="「🔲」Protectjoin「OFF」📵\n"
                                if msg.to in protectjoin: md+="「🔲」Protectinvite「ON」📲\n"
                                else: md+="「🔲」Protectinvite「OFF」📵\n"
                                if msg.to in protectkick: md+="「🔲」Protectkick「ON」📲\n"
                                else: md+="「🔲」Protectkick「OFF」📵\n"
                                if msg.to in protectcancel: md+="「🔲」Protectcancel「ON」📲\n"
                                else: md+="「🔲」Protectcancel「OFF」📵\n"
                                if msg.to in protectantijs: md+="「🔲」Antijs「ON」📲\n"
                                else: md+="「🔲」Antijs「OFF」📵\n"  
                                if msg.to in ghost: md+="「🔲」Ghost「ON」📲\n"
                                else: md+="「🔲」Ghost「OFF」📵\n"
                                ginfo = cl.getGroup(msg.to)
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 ✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺」\n• User : "
                                ret_ = "• Group : {}\n".format(str(ginfo.name))
                                ret_ += str(md)
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + "\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                
                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in admin:
                                cl.sendText(msg.to,"「ᴄʀᴇᴀᴛᴏʀ ʙᴏᴛs\✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺」") 
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd.startswith('about'):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            try:
                                arr = []
                                today = datetime.today()
                                thn = 2019 
                                bln = 12     #isi bulannya yg sewa
                                hr = 17    #isi tanggalnya yg sewa
                                future = datetime(thn, bln, hr)
                                days = (str(future - today))
                                comma = days.find(",")
                                days = days[:comma]
                                contact = cl.getContact(mid)
                                favoritelist = cl.getFavoriteMids()
                                grouplist = cl.getGroupIdsJoined()
                                contactlist = cl.getAllContactIds()
                                blockedlist = cl.getBlockedContactIds()
                                eltime = time.time() - mulai
                                bot = runtime(eltime)
                                start = time.time()
                                #cl.sendText("u6bca85cef34fc8ec0e2b459e179e3708", '.')
                                elapsed_time = time.time() - start
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 ɪɴғᴏʀᴍᴀsɪ sᴇʟғʙᴏᴛ 」\n• 🎴༎  ▶ᴜsᴇʀ : "
                                ret_ = "• 🎴༎  ༓ɢʀᴏᴜᴘ : {} ɢʀᴏᴜᴘ".format(str(len(grouplist)))
                                ret_ += "\n• 🎴༎▶ ༓ғʀɪᴇɴᴅ : {} ғʀɪᴇɴᴅ".format(str(len(contactlist)))
                                ret_ += "\n• 🎴༎▶ ༓ʙʟᴏᴄᴋᴇᴅ : {} ʙʟᴏᴄᴋᴇᴅ".format(str(len(blockedlist)))
                                ret_ += "\n• 🎴༎▶ ༓ғᴀᴠᴏʀɪᴛᴇ : {} ғᴀᴠᴏʀɪᴛᴇ".format(str(len(favoritelist)))
                                ret_ += "\n• 🎴༎▶ ༓ᴠᴇʀsɪᴏɴ : 「 sᴇʟғʙᴏᴛ ᴏɴʟʏ 」"
                                ret_ += "\n• 🎴༎▶ ༓ᴇxᴘɪʀᴇᴅ : {} - {} - {}".format(str(hr), str(bln), str(thn))
                                ret_ += "\n• 🎴༎▶ ༓ɪɴ ᴅᴀʏs : {} ᴀɢᴀɪɴ".format(days)
                                ret_ += "\n「 sᴘᴇᴇᴅ ʀᴇsᴘᴏɴ 」\n• 🎴༎▶  ༓{} ᴅᴇᴛɪᴋ".format(str(elapsed_time))
                                ret_ += "\n「 sᴇʟғʙᴏᴛ ʀᴜɴᴛɪᴍᴇ 」\n• 🎴༎▶  ༓{}".format(str(bot))
                                ret_ += "\n✅ʙʏ: ✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺"
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                #cl.sendContact(to, "")
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd == "me" or text.lower() == 'aim':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「 User Selfbot 」\n", "")
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage1(msg)

                        elif text.lower() == "mid":
                               cl.sendMessage(msg.to, msg._from)

                        elif cmd.startswith("mid "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Steal " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               a = channel.getProfileCoverURL(mid=key1)
                               cl.sendMessage(msg.to, "「 Contact Info 」\n• Nama : "+str(mi.displayName)+"\n• Mid : " +key1+"\n• Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                                   cl.sendImageWithURL(receiver, a)
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))
                                   cl.sendImageWithURL(receiver, a)

                        elif ("Cover " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = channel.getProfileCoverURL(mid=u)
                                    cl.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    cl.sendText(receiver, str(e))
#CLONE
                        elif cmd.startswith("clone "):
                          if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    cl.cloneContactProfile(ls)
                                    cl.sendContact(to, sender)
                                    cl.sendMessage(to, "➧ Berhasil clone profile")

                        elif cmd == "restoreprofile":
                            try:
                                lineProfile = cl.getProfile()
                                lineProfile.displayName = str(wait["myProfile"]["displayName"])
                                lineProfile.statusMessage = str(wait["myProfile"]["statusMessage"])
                                lineProfile.pictureStatus = str(wait["myProfile"]["pictureStatus"])
                                cl.updateProfileAttribute(8, lineProfile.pictureStatus)
                                cl.updateProfile(lineProfile)
                                coverId = str(wait["myProfile"]["coverId"])
                                cl.updateProfileCoverById(coverId)
                                cl.sendMessage(to, "ʀᴇsᴛᴏʀᴇ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs, ᴡᴀɪᴛ ᴀ ғᴇᴡ ᴍɪɴᴜᴛᴇs")
                            except Exception as e:
                                cl.sendMessage(to, "ʀᴇsᴛᴏʀᴇ ᴘʀᴏғɪʟᴇ ғᴀɪʟᴇᴅ")

                        elif cmd == "backupprofile":
                            try:
                                profile = cl.getProfile()
                                wait["myProfile"]["displayName"] = str(profile.displayName)
                                wait["myProfile"]["statusMessage"] = str(profile.statusMessage)
                                wait["myProfile"]["pictureStatus"] = str(profile.pictureStatus) #                        
                                cl.sendMessage(to, "ʙᴀᴄᴋᴜᴘ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs")
                            except Exception as e:
                                cl.sendMessage(to, "ʙᴀᴄᴋᴜᴘ ᴘʀᴏғɪʟᴇ ғᴀɪʟᴇᴅ")

                        elif ("Sticker: " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    query = msg.text.replace("Sticker: ", "")
                                    query = int(query)
                                    if type(query) == int:
                                        cl.sendImageWithURL(receiver, 'https://stickershop.line-scdn.net/stickershop/v1/product/'+str(query)+'/ANDROID/main.png')
                                        cl.sendText(receiver, 'https://line.me/S/sticker/'+str(query))
                                    else:
                                        cl.sendText(receiver, 'gunakan key sticker angka bukan huruf')
                                except Exception as e:
                                    cl.sendText(receiver, str(e))

                        elif "/ti/g/" in msg.text.lower():
                           if msg._from in admin:
                             if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                    if l not in n_links:
                                       n_links.append(l)
                                 for ticket_id in n_links:
                                    group = cl.findGroupByTicket(ticket_id)
                                    cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    cl.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                    
                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)
                                  cl.sendMessage(to, "Berhasil tolak sebanyak {} undangan grup".format(str(len(ginvited))))
                              else:
                                  cl.sendMessage(to, "Tidak ada undangan yang tertunda")

                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   ki.removeAllMessages(op.param2)
                                   kk.removeAllMessages(op.param2)
                                   kc.removeAllMessages(op.param2)
                                   kb.removeAllMessages(op.param2)
                                   kd.removeAllMessages(op.param2) 
                                   ke.removeAllMessages(op.param2)
                                   kf.removeAllMessages(op.param2)
                                   kg.removeAllMessages(op.param2)
                                   kh.removeAllMessages(op.param2)
                                   sw.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "remove chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   ki.removeAllMessages(op.param2)
                                   kk.removeAllMessages(op.param2)
                                   kc.removeAllMessages(op.param2)
                                   kb.removeAllMessages(op.param2)
                                   kd.removeAllMessages(op.param2)
                                   ke.removeAllMessages(op.param2)
                                   kf.removeAllMessages(op.param2)
                                   kg.removeAllMessages(op.param2)
                                  # kh.removeAllMessages(op.param2)
                                   sw.removeAllMessages(op.param2)
                                   cl.sendMessage(msg.to,"cнaт dιвerѕιнĸan...")
                                   ki.sendMessage(msg.to,"cнaт dιвerѕιнĸan...")
                                   kk.sendMessage(msg.to,"cнaт dιвerѕιнĸan...")
                                   kc.sendMessage(msg.to,"cнaт dιвerѕιнĸan...")
                                   kb.sendMessage(msg.to,"cнaт dιвerѕιнĸan...")
                                   kd.sendMessage(msg.to,"cнaт dιвerѕιнĸan...")
                                   ke.sendMessage(msg.to,"cнaт dιвerѕιнĸan...")
                                   kf.sendMessage(msg.to,"cнaт dιвerѕιнĸan...")
                                   kg.sendMessage(msg.to,"cнaт dιвerѕιнĸan...")
                                #   kh.sendMessage(msg.to,"cнaт dιвerѕιнĸan...")
                               except:
                                   pass

                        elif cmd.startswith("broadcast: "):
                           if msg._from in admin:
                             sep = text.split(" ")
                             bc = text.replace(sep[0] + " ","")
                             saya = cl.getGroupIdsJoined()
                             for group in saya:
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Broadcast 」\nBroadcast by "
                                ret_ = "{}".format(str(bc))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(group, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd.startswith("leave "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    ki.leaveGroup(i)
                                    kk.leaveGroup(i)
                                    kc.leaveGroup(i)
                                    kb.leaveGroup(i)
                                    kd.leaveGroup(i)
                                    ke.leaveGroup(i)
                                    kf.leaveGroup(i)
                                    kg.leaveGroup(i)
                                   # kh.leaveGroup(i)
                                    cl.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))

                                
                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 Status Setkey 」\nSetkey saat ini「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendMessage(msg.to, "「 Change Setkey 」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               cl.sendMessage(msg.to, "「 Resetkey 」\nSetkey mu telah direset")

                        elif cmd == "reset":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「 ʀᴇsᴛᴀʀᴛɪɴɢ 」\nUser ", "\nᴘʀᴏsᴇss...ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ ʙᴏss")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                eltime = time.time() - mulai
                                bot = runtime(eltime)
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Runtime 」\n• User Self : "
                                ret_ = "• {}".format(str(bot))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "「 Group Info 」\n「✭」 ➣ ɴᴀᴍᴀ ɢʀᴜᴘ : {}".format(G.name)+ "\n「✭」 ID Group : {}".format(G.id)+ "\n「✭」 Pembuat : {}".format(G.creator.displayName)+ "\n「✭」 Waktu Dibuat : {}".format(str(timeCreated))+ "\n「✭」 Jumlah Member : {}".format(str(len(G.members)))+ "\n「✭」 Jumlah Pending : {}".format(gPending)+ "\n「✭」 Group Qr : {}".format(gQr)+ "\n「✭」 Group Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "「 Group Info 」"
                                ret_ += "\n「⭐」  ɴᴀᴍᴀ ɢʀᴜᴘ : {}".format(G.name)
                                ret_ += "\n「⭐」 ID Group : {}".format(G.id)
                                ret_ += "\n「⭐」 Pembuat : {}".format(gCreator)
                                ret_ += "\n「⭐」 Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n「⭐」 Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n「⭐」 Jumlah Pending : {}".format(gPending)
                                ret_ += "\n「⭐」 Group Qr : {}".format(gQr)
                                ret_ += "\n「⭐」 Group Ticket : {}".format(gTicket)
                                ret_ += "\n「⭐」 Picture Url : http://dl.profile.line-cdn.net/{}".format(G.pictureStatus)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except:
                                pass
#Spamcallto
                        elif cmd.startswith("spamcallto"):
                          dan = text.split(" ")
                          num = int(dan[1])                      
                          if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                     if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                for ls in lists:
                                 for var in range(0,num):
                                      group = cl.getGroup(to)
                                      members = [ls]
                                      cl.acquireGroupCallRoute(to)
                                      cl.inviteIntoGroupCall(to, contactIds=members) #                           
                                cl.sendMessage(msg.to, "Berhasil Sct ")

                        elif cmd.startswith("open "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                try:
                                    gCreator = G.creator.mid
                                    dia = cl.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = '「 Sukses Open Qr 」\n• Creator :  '
                                    diaa = str(dia.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += xpesan+zxc
                                ret_ += "• ▶Nama : {}".format(G.name)
                                ret_ += "\n• ▶Group Qr : {}".format(gQr)
                                ret_ += "\n• ▶Pendingan : {}".format(gPending)
                                ret_ += "\n• ▶Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except:
                                pass

                        elif cmd.startswith("close "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                try:
                                    gCreator = G.creator.mid
                                    dia = cl.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = '「 Sukses Close Qr 」\n• Creator :  '
                                    diaa = str(dia.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += xpesan+zxc
                                ret_ += "• ▶Nama : {}".format(G.name)
                                ret_ += "\n• ▶Group Qr : {}".format(gQr)
                                ret_ += "\n• ▶Pendingan : {}".format(gPending)
                                ret_ += "\n• ▶Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except:
                                pass
                                
                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "「⭐」 "+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"「⭐」 Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("protectqr on "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    protectqr[G] = True
                                    f=codecs.open('protectqr.json','w','utf-8')
                                    json.dump(protectqr, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    gCreator = G.creator.mid
                                    dia = cl.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = '「 Protect Qr Diaktifkan 」\n• Creator :  '
                                    diaa = str(dia.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                except:
                                    cl.sendText(msg.to, "Grup itu tidak ada")
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += xpesan+zxc
                                ret_ += "• ▶Nama grup : {}".format(G.name)
                                ret_ += "\n• ▶Pendingan : {}".format(gPending)
                                ret_ += "\n• ▶Jumlah Member : {}".format(str(len(G.members)))
                                cl.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except Exception as e:
                                cl.sendMessage(to, str(e))

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               ki.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist2":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kk.getGroupIdsJoined()
                               for i in gid:
                                   G = kk.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kk.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist3":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc.getGroupIdsJoined()
                               for i in gid:
                                   G = kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kc.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")
                               
                        elif cmd == "gruplist4":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kb.getGroupIdsJoined()
                               for i in gid:
                                   G = kb.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kb.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Opened")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Closed")

                        elif cmd == "url":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "Grup "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)
#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "cpp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["ARfoto"][mid] = True
                                cl.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd == "cvp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["ARvideo"][mid] = True
                                cl.sendText(msg.to,"Kirim videonya.....")

                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Nama diganti jadi " + string + "")
#KICKALL
                        elif "!!curut" in msg.text:
                          if msg._from in admin:
                           if msg.toType == 2:
                              print("ok")
                              _name = msg.text.replace("!!curut","")
                              gs = cl.getGroup(msg.to)
                              gs = cl.getGroup(msg.to)
                              gs = cl.getGroup(msg.to)
                              targets = []
                              for g in gs.members:
                                 if _name in g.displayName:
                                     targets.append(g.mid)
                              if targets == []:
                                 cl.sendText(msg.to,"Tidak Ditemukan.")
                              else:
                                  for target in targets:
                                   if not target in admin and Bots:
                                      try:
                                          klist=[cl]
                                          kicker=random.choice(klist)
                                          kicker.kickoutFromGroup(msg.to,[target])
                                          print (msg.to,[g.mid])
                                      except Exception as e:
                                          break

                        elif "!terx" in msg.text:                      	
                           if msg._from in Bots:
                            if msg.toType == 2:
                               print                               
                               _name = msg.text.replace("!terx","")
                               gs = ki.getGroup(msg.to)
                               gs = kk.getGroup(msg.to)
                               gs = kc.getGroup(msg.to) 
                               gs = kb.getGroup(msg.to)    
                               gs = kd.getGroup(msg.to)
                               gs = ke.getGroup(msg.to)
                               gs = kf.getGroup(msg.to)
                               gs = kj.getGroup(msg.to)
                               gs = sw.getGroup(msg.to)
                               ki.sendMessage(msg.to,"ASSALAMUALAIKUM")
                               ki.sendMessage(msg.to,"Halo\n"
 "ASSALAMUALAIKUM\n"
"  ╭━TERX-BOT-SADIS\n"
"  ╰╮┏━┳┳┓┏┳┳┓┏┳┳┳┓\n"
"  ┏┻╋━┻┻┫┣┻┻┫┣┻┻┻┫\n"
"  ┃HAY▪┃KMI DTANG LGI┃\n"
"  ┗ⓞⓞ┻┻ⓞ━━ⓞ┻┻ⓞ━╯\n"
"UNTUK MEMBAKAR\nROOM KALIAN\n"
"..  (҂`_´)\n"
   " <,︻╦̵̵̿╤━ ҉     ~  •"
"█۞███████]▄▄▄▄▄▄▃●●\n"
"▂▄▅█████████▅▄▃▂…"
"[██████████████████]\n"
"◥⊙⊙▲⊙▲⊙▲⊙▲⊙▲⊙\n"
"╭━╮╭━╮\n"
"┃┃╰╯┃┃\n"
"┃╭╮╭╮┣┳━╮╭━━┳━━┳┳━╮\n"
"┃┃┃┃┃┣┫╭╮┫╭╮┃╭╮┣┫╭╯\n"
"┃┃┃┃┃┃┃┃┃┃╰╯┃╰╯┃┃┃\n"
"╰╯╰╯╰┻┻╯╰┻━╮┣━╮┣┻╯\n"
"╱╱╱╱╱╱╱╱╱╭━╯┣━╯┃\n"
"╱╱╱╱╱╱╱╱╱╰━━┻━━╯\n"
"━━━━━━━━━━━━━"
"TANPA BANYAK NGEMENG"
"GUE SITA ROOM KALIAN\n" 
"JANGAN NANGIS JANGAN MLONGO\n"
"AYO TANGKIS KLO MAMPU\n"
"━━━━━━━━━━━━━\n"
	"╔══╗╔═╗╔══╗╔═╦═╗\n"
	"╚╗╔╝║╦╝║╔╗║║║║║║\n"
	"━║║━║╩╗║╠╣║║║║║║\n"
	"━╚╝━╚═╝╚╝╚╝╚╩═╩╝\n"
"━━━━━━━━━━━━━\n"
	"TEAM-SADIS\n"
	"GAK PERNAH BIKIN ULAH\n"
	"MAKA KALI INI MARAH\n"
	"TEAM-SADIS NGAMUK\n"
	"TANGKIS KLO KLIAN MAMPU\n"
	"JANGAN SOK LO YA AMA TEAM KAMI\n"
"━━━━━━━━━━━━━\n"        
"TEAM TERX-BOTS-SADIS\n"
"***SADIS KILER***\n" 
"TAR-TER-TAR-TOR\n"
		"╔═╗╔══╗╔══╗╔══╗\n"
		"║╬║║╔╗║╚╗╔╝║╔╗║\n"
		"║╗╣║╠╣║━║║━║╠╣║\n"
		"╚╩╝╚╝╚╝━╚╝━╚╝╚╝\n"
		"━━━━━━━━━━━━━━━\n"
		"╔═╗╔══╗╔══╗╔══╗\n"
		"║╬║║╔╗║╚╗╔╝║╔╗║\n"
		"║╗╣║╠╣║━║║━║╠╣║\n"
		"╚╩╝╚╝╚╝━╚╝━╚╝╚╝\n"
		"━━━━━━━━━━━━━━━\n"
		"╔═╗╔══╗╔══╗╔══╗\n"
		"║╬║║╔╗║╚╗╔╝║╔╗║\n"
		"║╗╣║╠╣║━║║━║╠╣║\n"
		"╚╩╝╚╝╚╝━╚╝━╚╝╚╝\n"
		"━━━━━━━━━━━━━━━\n"
">>>lain x jangan sok songong ama kami>><\ningat  yee,,klo lu dendam cari kami\n<<<<<<<<<>>\nhttp://line.me/ti/p/~gerhanaselatan\nhttp://line.me/ti/p/~cyberline11")
                               targets = []
                               for g in gs.members:
                                   if _name in g.displayName:
                                       targets.append(g.mid)
                               if targets == []:
                                  ki.sendMessage(msg.to,"Not found")
                              #    else:
                               for target in targets:
                                     if target not in Bots:
                                      try:
                                          klist=[ki,kk,kc,kb,kd,ke,kf,kj,sw]
                                          kicker=random.choice(klist)
                                          kicker.kickoutFromGroup(msg.to,[target])
                                          print (msg.to,[g.mid])
                                      except:
                                          kc.sendMessage(msg.to,"I'm Sory")
                        elif ("Kick " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif cmd == "bot1up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Amid] = True
                                ki.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "bot2up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Bmid] = True
                                kk.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "bot3up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Cmid] = True
                                kc.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "bot4up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Dmid] = True
                                kb.sendMessage(msg.to,"Send your images.....")
        
                        elif cmd == "bot5up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Emid] = True
                                kd.sendMessage(msg.to,"Send your images.....")         
                                
                        elif cmd == "bot6up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Fmid] = True
                                ke.sendMessage(msg.to,"Send your images.....")        
                                
                        elif cmd == "bot7up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Gmid] = True
                                kf.sendMessage(msg.to,"Send your images.....")       
                                
                        elif cmd == "bot8up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Jmid] = True
                                kj.sendMessage(msg.to,"Send your images.....")         
                                
                        elif cmd == "bot9up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Zmid] = True
                                sw.sendMessage(msg.to,"Send your images.....")      
                                
                        elif cmd == "bot10up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Zmid] = True
                                sw.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "bot112up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Zmid] = True
                                sw.sendMessage(msg.to,"Send your images.....")

                        elif cmd.startswith("bot1name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot2name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kk.getProfile()
                                profile.displayName = string
                                kk.updateProfile(profile)
                                kk.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot3name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("bot4name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kb.getProfile()
                                profile.displayName = string
                                kb.updateProfile(profile)
                                kb.sendMessage(msg.to,"Nama diganti jadi " + string + "")    
   
                        elif cmd.startswith("bot5name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kd.getProfile()
                                profile.displayName = string
                                kd.updateProfile(profile)
                                kd.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot6name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ke.getProfile()
                                profile.displayName = string
                                ke.updateProfile(profile)
                                ke.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot7name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kf.getProfile()
                                profile.displayName = string
                                kf.updateProfile(profile)
                                kf.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot8name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kj.getProfile()
                                profile.displayName = string
                                kj.updateProfile(profile)
                                kj.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("bot9name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                sw.sendMessage(msg.to,"Nama diganti jadi " + string + "")       

                        elif cmd.startswith("bot10name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                sw.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("bot11name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                sw.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd == "kibar":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendContact(to, mid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Emid)
                               cl.sendContact(to, Fmid)
                               cl.sendContact(to, Gmid)
                               cl.sendContact(to, Jmid)
                               cl.sendContact(to, Zmid)
                               cl.sendMessage(msg.to, "█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
 "ASSALAMUALAIKUM\n"
"  ╭━ⒹTERX-BOTS\n"
"  ╰╮┏━┳┳┓┏┳┳┓┏┳┳┳┓\n"
"  ┏┻╋━┻┻┫┣┻┻┫┣┻┻┻┫\n"
"  ┃HAY▪┃KMI DTANG LGI┃\n"
"  ┗ⓞⓞ┻┻ⓞ━━ⓞ┻┻ⓞ━╯\n"
"UNTUK MEMBAKAR\nROOM KALIAN\n"
"..  (҂`_´)\n"
   " <,︻╦̵̵̿╤━ ҉     ~  •"
"█۞███████]▄▄▄▄▄▄▃●●\n"
"▂▄▅█████████▅▄▃▂…"
"[██████████████████]\n"
"◥⊙⊙▲⊙▲⊙▲⊙▲⊙▲⊙\n"
"╭━╮╭━╮\n"
"┃┃╰╯┃┃\n"
"┃╭╮╭╮┣┳━╮╭━━┳━━┳┳━╮\n"
"┃┃┃┃┃┣┫╭╮┫╭╮┃╭╮┣┫╭╯\n"
"┃┃┃┃┃┃┃┃┃┃╰╯┃╰╯┃┃┃\n"
"╰╯╰╯╰┻┻╯╰┻━╮┣━╮┣┻╯\n"
"╱╱╱╱╱╱╱╱╱╭━╯┣━╯┃\n"
"╱╱╱╱╱╱╱╱╱╰━━┻━━╯\n"
"━━━━━━━━━━━━━"
"TANPA BANYAK NGEMENG\n"
"GUE SITA ROOM KALIAN\n" 
"JANGAN NANGIS JANGAN MLONGO\n"
"AYO TANGKIS KLO MAMPU\n"
"━━━━━━━━━━━━━\n"
	"╔══╗╔═╗╔══╗╔═╦═╗\n"
	"╚╗╔╝║╦╝║╔╗║║║║║║\n"
	"━║║━║╩╗║╠╣║║║║║║\n"
	"━╚╝━╚═╝╚╝╚╝╚╩═╩╝\n"
"━━━━━━━━━━━━━\n"
	"TEAM-SADIS\n"
	"GAK PERNAH BIKIN ULAH\n"
	"MAKA KALI INI MARAH\n\n"
	"TEAM SADIS NGAMUK\n"
"━━━━━━━━━"        
"TANGKIS KLO KLIAN MAMPU\n"
"JANGAN SOK LO YA AMA TEAM KAMI\n"
"TEAM -SADIS\n"

		"╔═╗╔══╗╔══╗╔══╗\n"
		"║╬║║╔╗║╚╗╔╝║╔╗║\n"
		"║╗╣║╠╣║━║║━║╠╣║\n"
		"╚╩╝╚╝╚╝━╚╝━╚╝╚╝\n"
		"━━━━━━━━━━━━━━━\n"
		"╔═╗╔══╗╔══╗╔══╗\n"
		"║╬║║╔╗║╚╗╔╝║╔╗║\n"
		"║╗╣║╠╣║━║║━║╠╣║\n"
		"╚╩╝╚╝╚╝━╚╝━╚╝╚╝\n"
		"━━━━━━━━━━━━━━━\n"
		"╔═╗╔══╗╔══╗╔══╗\n"
		"║╬║║╔╗║╚╗╔╝║╔╗║\n"
		"║╗╣║╠╣║━║║━║╠╣║\n"
		"╚╩╝╚╝╚╝━╚╝━╚╝╚╝\n"
		"━━━━━━━━━━━━━━━\n"
		"TEAM TERX-BOTS-SADIS\n"
		"***SADIS KILER***\n" 
">>>lain x jangan sok songong ama kami>><\ningat  yee,,klo lu dendam cari kami\n<<<<<<<<<>>\nhttp://line.me/ti/p/~gerhanaselatan\nhttp://line.me/ti/p/~cyberline11")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"15996978","STKPKGID":"1416471","STKVER":"1"}, contentType=7)

                     #   elif cmd == "reinvite":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                kb.leaveGroup(msg.to)
                                kd.leaveGroup(msg.to)
                                ke.leaveGroup(msg.to)
                                kf.leaveGroup(msg.to)
                                kj.leaveGroup(msg.to)
                                sw.leaveGroup(msg.to)
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                ki.updateGroup(G)

                        elif cmd == "terx" or cmd == "terxbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               cl.sendMessage(msg.to, "[TERX-BOTS-SADIS].")
                               elapsed_time = time.time() - start
                               ki.sendMessage(msg.to, "ready\nвoѕѕ".format(str(elapsed_time)))
                               kk.sendMessage(msg.to, "ready\nвoѕѕ".format(str(elapsed_time)))
                               kc.sendMessage(msg.to, "ready\nвoѕѕ".format(str(elapsed_time)))
                               kb.sendMessage(msg.to, "ready\nвoѕѕ".format(str(elapsed_time)))
                               kd.sendMessage(msg.to, "ready\nвoѕѕ".format(str(elapsed_time)))
                               ke.sendMessage(msg.to, "ready\nвoѕѕ".format(str(elapsed_time)))
                               kf.sendMessage(msg.to, "ready\nвoѕѕ".format(str(elapsed_time)))
                               kj.sendMessage(msg.to, "ready\nвoѕѕ".format(str(elapsed_time)))
                               sw.sendMessage(msg.to, "[all ѕтay вoѕѕ]")
                               cl.sendMessage(msg.to, "тerĸendalι\nвoѕѕ")


                        elif cmd == "harga":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "╭══════════\n║─[     DAFTAR HARGA     ]─ \n║SELFBOT ONLY = 75K /BLN\n║2 ASSIST = 100K /BLN\n║5 ASSIST = 200K /BLN\n║10 ASSIST = 300K /BLN\n║\n║PROTECT ANTIJS\n║\n║2 BOT + ANTIJS = 150K /BLN\n║5 BOT + ANTIJS = 300K /BLN\n║10 BOT + ANTIJS = 400K /BLN\n║\n║\═MINAT\n║ SILAHKAN ADD CONTACT \n║ DIBAWAH INI   \n║\n║http://line.me/ti/p/~gerhanaselatan\n║       MAKASIIH      \n║\n╰════════════")
                               cl.sendMessage(msg.to, "Yuk yg minat di order.... ")
                               cl.sendContact(to, mid)

                        elif "Gass" in msg.text:
                           if msg._from in Bots:
                            if msg.toType == 2:
                             #  print "Otw cleanse"
                               _name = msg.text.replace("Gass","")
                               gs = ki.getGroup(msg.to)
                               gs = kk.getGroup(msg.to)
                               gs = kc.getGroup(msg.to) 
                               gs = kb.getGroup(msg.to)    
                               gs = kd.getGroup(msg.to)
                               gs = ke.getGroup(msg.to)
                               gs = kf.getGroup(msg.to)
                               gs = kj.getGroup(msg.to)
                               gs = sw.getGroup(msg.to)
                              # gs = #k3.getGroup(msg.to)
                               #gs = #k4.getGroup(msg.to)
                               #gs = #k5.getGroup(msg.to)
                              # gs = #k6.getGroup(msg.to)
                               #gs = #k7.getGroup(msg.to)
                               cl.sendMessage(to, "█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\nASSALAMUALAIKUM\n")
                               ki.sendMessage(to, 
"  ╭━TEAM SADIS\n"
"  ╰╮┏━┳┳┓┏┳┳┓┏┳┳┳┓\n"
"  ┏┻╋━┻┻┫┣┻┻┫┣┻┻┻┫\n"
"  ┃HAY▪┃KMI DATANG LGI┃" 
" ┃┗ⓞⓞ┻┻ⓞ━━ⓞ┻┻ⓞ━╯\n"
"UNTUK MEMBAKAR ROOMKALIAN\n"
"..  (҂`_´)\n"
   " <,︻╦̵̵̿╤━ ҉     ~  •"
"█۞███████]▄▄▄▄▄▃●●\n"
"▂▄▅█████████▅▄▃▂…"
"[█████████████████]\n"
"◥⊙▲⊙▲⊙▲⊙▲⊙⊙▲⊙")
                               kk.sendMessage(to, 
"━━━━━━━━━━━━━━\n"
"..  (҂`_´)\n"
   " <,︻╦̵̵̿╤━ ҉     ~  •"
"█۞███████]▄▄▄▄▄▃●●\n"
"▂▄▅█████████▅▄▃▂…"
"[█████████████████]\n"
"◥⊙▲⊙▲⊙▲⊙▲⊙⊙▲⊙\n"
"╭━╮╭━╮\n"
"┃┃╰╯┃┃\n"
"┃╭╮╭╮┣┳━╮╭━━┳━━┳┳━╮\n"
"┃┃┃┃┃┣┫╭╮┫╭╮┃╭╮┣┫╭╯\n"
"┃┃┃┃┃┃┃┃┃┃╰╯┃╰╯┃┃┃\n"
"╰╯╰╯╰┻┻╯╰┻━╮┣━╮┣┻╯\n"
"╱╱╱╱╱╱╱╱╱╭━╯┣━╯┃\n"
"╱╱╱╱╱╱╱╱╱╰━━┻━━╯\n"
"━━━━━━━━━━━━━━ \n"
"╭━╮╭━╮\n"
"┃┃╰╯┃┃\n"
"┃╭╮╭╮┣┳━╮╭━━┳━━┳┳━╮\n"
"┃┃┃┃┃┣┫╭╮┫╭╮┃╭╮┣┫╭╯\n"
"┃┃┃┃┃┃┃┃┃┃╰╯┃╰╯┃┃┃\n"
"╰╯╰╯╰┻┻╯╰┻━╮┣━╮┣┻╯\n"
"╱╱╱╱╱╱╱╱╱╭━╯┣━╯┃\n"
"╱╱╱╱╱╱╱╱╱╰━━┻━━╯\n"
"━━━━━━━━━━━━━━"
"TANPA BANYAK NGEMENG\n"
"GUE SITA ROOM KALIAN\n" 
"JANGAN NANGIS JANGAN MLONGO\n"
"AYO TANGKIS KLO MAMPU\n"
"━━━━━━━━━━━━━━\n"
	"╔══╗╔═╗╔══╗╔═╦═╗\n"
	"╚╗╔╝║╦╝║╔╗║║║║║║\n"
	"━║║━║╩╗║╠╣║║║║║║\n"
	"━╚╝━╚═╝╚╝╚╝╚╩═╩╝\n"
"━━━━━━━━━━━━━━\n"
	"TEAM TERX-BOTS-SADIS\n"
	"GAK PERNAH BIKIN ULAH\n"
	"MAKA KALI INI KAMI MARAH\n"
	"TERX-BOTS-SADIS NGAMUK\n"
"━━━━━━━━━━━━━━\n"        
"TANGKIS KLO KLIAN MAMPU\n"
"TANGKIS KLO KLIAN MAMPU\n"
"JANGAN SOK LO YA AMA TEAM KAMI\n"
"TEAM TERX-BOTS-SADIS\n"
"***SADIS KILER***\n" 
        #                       kc.sendMessage(msg.to,
">>>lain x jangan sok songong ama kami>><\ningat  yee,,klo lu dendam cari kami\n<<<<<<<<<>>\nhttp://line.me/ti/p/~gerhanaselatan\nhttp://line.me/ti/p/~cyberline11")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"24893204","STKPKGID":"1790925","STKVER":"1"}, contentType=7)
                               targets = []
                               for g in gs.members:
                                   if _name in g.displayName:
                                       targets.append(g.mid)
                               if targets == []:
                                  ki.sendMessage(msg.to,"Not found")
                              #    else:
                               for target in targets:
                                     if target not in Bots:
                                      try:
                                          klist=[ki,kk,kb,kc,kb,kd,ke,kg,kj,sw]
                                          kicker=random.choice(klist)
                                          kicker.kickoutFromGroup(msg.to,[target])
                                          print (msg.to,[g.mid])
                                      except:
                                          cl.sendMessage(msg.to,"Bye all")
                        elif ("Kick " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                    #    elif cmd == "terx.reinvite":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                kb.leaveGroup(msg.to)
                                kd.leaveGroup(msg.to)
                                ke.leaveGroup(msg.to)
                                kf.leaveGroup(msg.to)
                                kg.leaveGroup(msg.to)
                                kh.leaveGroup(msg.to)
                                kj.leaveGroup(msg.to)
                                sw.leaveGroup(msg.to)
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                ki.updateGroup(G)

                        elif cmd == "mlebu": #mode invite
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid]
                                    cl.inviteIntoGroup(msg.to, anggota)
                                    ki.acceptGroupInvitation(msg.to)
                                    kk.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    kb.acceptGroupInvitation(msg.to)
                                    kd.acceptGroupInvitation(msg.to)
                                    ke.acceptGroupInvitation(msg.to)
                                    kf.acceptGroupInvitation(msg.to)
                                    cl.sendMessage(msg.to,"Grup "+str(ginfo.name)+"Aman Dari JS")
                                except:
                                    pass

                        elif cmd == "cb":
                            if msg._from in admin:
                                try:cl.inviteIntoGroup(to, ["uc5abb77929c76b5f91f4beaecd88e5e2"]);has = "OK"
                                except:has = "NOT"
                                try:cl.kickoutFromGroup(to, ["uc5abb77929c76b5f91f4beaecd88e5e2"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sᴛʀᴏɴɢ"
                                else:sil = "sᴇᴋᴀʀᴀᴛ"
                                if has1 == "OK":sil1 = "sᴛʀᴏɴɢ"
                                else:sil1 = "sᴇᴋᴀʀᴀᴛ"
                                cl.sendMessage(to, "🇴sᴛᴀᴍɪɴᴀ🇴\n▶ᴋɪᴄᴋ : {} \n▶ɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                                try:ki.inviteIntoGroup(to, ["u7abc6bc75b34fc0c545fe46c43cff380"]);has = "OK"
                                except:has = "NOT"
                                try:ki.kickoutFromGroup(to, ["u7abc6bc75b34fc0c545fe46c43cff380"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sᴛʀᴏɴɢ"
                                else:sil = "sᴇᴋᴀʀᴀᴛ"
                                if has1 == "OK":sil1 = "sᴛʀᴏɴɢ"
                                else:sil1 = "sᴇᴋᴀʀᴀᴛ"
                                ki.sendMessage(to, "🇴sᴛᴀᴍɪɴᴀ🇴\n▶ᴋɪᴄᴋ : {} \n▶ɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                                try:kk.inviteIntoGroup(to, ["ub4b2144cb807203fe8ab26ee90ea3804"]);has = "OK"
                                except:has = "NOT"
                                try:kk.kickoutFromGroup(to, ["ub4b2144cb807203fe8ab26ee90ea3804"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sᴛʀᴏɴɢ"
                                else:sil = "sᴇᴋᴀʀᴀᴛ"
                                if has1 == "OK":sil1 = "sᴛʀᴏɴɢ"
                                else:sil1 = "sᴇᴋᴀʀᴀᴛ"
                                kk.sendMessage(to, "🇴sᴛᴀᴍɪɴᴀ🇴\n▶ᴋɪᴄᴋ : {} \n▶ɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                                try:kc.inviteIntoGroup(to, ["uae95a5f98fec6ca04407a4fba451662f"]);has = "OK"
                                except:has = "NOT"
                                try:kc.kickoutFromGroup(to, ["uae95a5f98fec6ca04407a4fba451662f"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sᴛʀᴏɴɢ"
                                else:sil = "sᴇᴋᴀʀᴀᴛ"
                                if has1 == "OK":sil1 = "sᴛʀᴏɴɢ"
                                else:sil1 = "sᴇᴋᴀʀᴀᴛ"
                                kc.sendMessage(to, "🇴sᴛᴀᴍɪɴᴀ🇴\n▶ᴋɪᴄᴋ : {} \n▶ɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                                try:kb.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                except:has = "NOT"
                                try:kb.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sᴛʀᴏɴɢ"
                                else:sil = "sᴇᴋᴀʀᴀᴛ"
                                if has1 == "OK":sil1 = "sᴛʀᴏɴɢ"
                                else:sil1 = "sᴇᴋᴀʀᴀᴛ"
                                kb.sendMessage(to, "🇴sᴛᴀᴍɪɴᴀ🇴\n▶ᴋɪᴄᴋ : {} \n▶ɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                                try:kd.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                except:has = "NOT"
                                try:kd.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sᴛʀᴏɴɢ"
                                else:sil = "sᴇᴋᴀʀᴀᴛ"
                                if has1 == "OK":sil1 = "sᴛʀᴏɴɢ"
                                else:sil1 = "sᴇᴋᴀʀᴀᴛ"
                                kd.sendMessage(to, "🇴sᴛᴀᴍɪɴᴀ🇴\n▶ᴋɪᴄᴋ : {} \n▶ɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                                try:ke.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                except:has = "NOT"
                                try:ke.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sᴛʀᴏɴɢ"
                                else:sil = "sᴇᴋᴀʀᴀᴛ"
                                if has1 == "OK":sil1 = "sᴛʀᴏɴɢ"
                                else:sil1 = "sᴇᴋᴀʀᴀᴛ"
                                ke.sendMessage(to, "🇴sᴛᴀᴍɪɴᴀ🇴\n▶ᴋɪᴄᴋ : {} \n▶ɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                                try:kf.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                except:has = "NOT"
                                try:kf.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sᴛʀᴏɴɢ"
                                else:sil = "sᴇᴋᴀʀᴀᴛ"
                                if has1 == "OK":sil1 = "sᴛʀᴏɴɢ"
                                else:sil1 = "sᴇᴋᴀʀᴀᴛ"
                                kf.sendMessage(to, "🇴sᴛᴀᴍɪɴᴀ🇴\n▶ᴋɪᴄᴋ : {} \n▶ɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                                try:kj.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                except:has = "NOT"
                                try:kj.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sᴛʀᴏɴɢ"
                                else:sil = "sᴇᴋᴀʀᴀᴛ"
                                if has1 == "OK":sil1 = "sᴛʀᴏɴɢ"
                                else:sil1 = "sᴇᴋᴀʀᴀᴛ"
                                kj.sendMessage(to, "🇴sᴛᴀᴍɪɴᴀ🇴\n▶ᴋɪᴄᴋ : {} \n▶ɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                                try:sw.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                except:has = "NOT"
                                try:sw.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sᴛʀᴏɴɢ"
                                else:sil = "sᴇᴋᴀʀᴀᴛ"
                                if has1 == "OK":sil1 = "sᴛʀᴏɴɢ"
                                else:sil1 = "sᴇᴋᴀʀᴀᴛ"
                                sw.sendMessage(to, "🇴sᴛᴀᴍɪɴᴀ🇴\n▶ᴋɪᴄᴋ : {} \n▶ɪɴᴠɪᴛᴇ : {}".format(sil1,sil))

                        elif cmd == "ghost in":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kj.sendMessage(msg.to, "Ghost masuk "+str(G.name))
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                sw.sendMessage(msg.to, "Ghost masuk "+str(G.name))
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "ghost out":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                kj.sendMessage(msg.to, "Ghost dipaksah Out "+str(G.name))
                                kj.leaveGroup(msg.to)
                                sw.sendMessage(msg.to, "Ghost dipaksah Out "+str(G.name))
                                sw.leaveGroup(msg.to)

                        elif cmd == "respon" or cmd == "crew":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                cl.sendMessage(msg.to, "✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺")
                                ki.sendMessage(msg.to, "✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺")
                                kk.sendMessage(msg.to, "✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺")
                                kc.sendMessage(msg.to, "✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺")
                                kb.sendMessage(msg.to, "✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺")
                                kd.sendMessage(msg.to, "✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺")
                                ke.sendMessage(msg.to, "✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺")
                                kf.sendMessage(msg.to, "✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺")
                                kj.sendMessage(msg.to, "✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺")
                                sw.sendMessage(msg.to, "✺[α̲̲̅̅υ̲̲̅̅т̲̲̅̅i̲̲̅̅s̲̲̅̅ ̲̲̅̅b̲̲̅̅σ̲̲̅̅т̲̲̅̅s̲̅]✺")
                            #    cl.sendMessage(msg.to, "╔═══╗\n║╔═╗║\n║║─║╠╗╔╦══╦═╗\n║╚═╝║╚╝║╔╗║╔╗╗\n║╔═╗║║║║╔╗║║║║\n╚╝─╚╩╩╩╩╝╚╩╝╚╝")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "cekban" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                cl.sendMessage(msg.to,"ᴛɪᴅᴀᴋ ᴀᴅᴀ ʙᴀᴄᴋʟɪsᴛ")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"🔳 Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"🔲 Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

#===========BOT UPDATE============#

#===========BOT UPDATE============#
                        elif msg.text in ["Nek","Tagall","Desah","Tag","Assalamualaikum","Tag all","Siang","Sore","Malam","Nahh","All"]:
                               if wait["selfbot"] == True:
                                if msg._from in admin:
                                 group = cl.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//20
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*20 : (a+1)*20]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Zero \n'
                                    cl.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)  

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"「 Daftar User Bot 」\n\n"+ma+"\nTotal「%s」List Bots" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    a = a + 1
                                    end = '\n'
                                    mb += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    a = a + 1
                                    end = '\n'
                                    mc += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"「 ᴅᴀғᴛᴀʀ ᴀᴅᴍɪɴ 」\n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotal「%s」Pengguna Selfbot" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "!bye":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.sendText(msg.to, "Bye bye fams "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, "「 Respontime 」\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               sendMention(msg.to, sender, "\n• ", "")
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to,"Zzzz...{}detik".format(str(elapsed_time)))
                                
                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['RAreadPoint'][msg.to] = msg_id
                                 Setmain['RAreadMember'][msg.to] = {}
                                 cl.sendText(msg.to, "「 Status Lurking 」\nBerhasil diaktifkan, selanjutnya ketik lurkers\n\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d'))
                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['RAreadPoint'][msg.to]
                                 del Setmain['RAreadMember'][msg.to]
                                 cl.sendText(msg.to, "「 Status Lurking 」\nBerhasil dimatikan\n\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d'))
                            
                        elif cmd == "lurkers":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            if msg.to in Setmain['RAreadPoint']:
                                if Setmain['RAreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['RAreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  「 Daftar Member 」    \n\n 「 Total {} Sider 」\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['RAreadPoint'][msg.to]
                                        del Setmain['RAreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['RAreadPoint'][msg.to] = msg.id
                                    Setmain['RAreadMember'][msg.to] = {}
                                else:
                                    cl.sendText(msg.to, "User kosong...")
                            else:
                                cl.sendText(msg.to, "Ketik lurking on dulu")

                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "「 sᴛᴀᴛᴜs sɪᴅᴇʀ 」\n✅ʙᴇʀʜᴀsɪʟ ᴅɪᴀᴋᴛɪғᴋᴀɴ\n\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d'))
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "「 Status Sider 」\n🎴ʙᴇʀʜᴀsɪʟ ᴅɪᴍᴀᴛɪᴋᴀɴ\n\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d'))
                              else:
                                  cl.sendMessage(msg.to, "🎴sᴜᴅᴀʜ ᴛɪᴅᴀᴋ ᴀᴋᴛɪғ")

#===========Hiburan============#
                        elif cmd.startswith("get-audio "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            query = msg.text.replace(sep[0] + " "," ")
                            cond = query.split("|")
                            search = str(cond[0])
                            with requests.session() as web:
                                web.headers["User-Agent"] = "Mozilla/5.0"
                                result = web.get("https://farzain.xyz/api/premium/yt_search.php?apikey=apikey_saintsbot&id={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    if data["respons"] != []:
                                        num = 0
                                        ret_ = "「 Pencarian Audio 」\n"
                                        for res in data["respons"]:
                                            num += 1
                                            ret_ += "\n {}. {}".format(str(num), str(res['title']))
                                        ret_ += "\n\n Total {} Result".format(str(len(data["respons"])))
                                        cl.sendMessage(msg.to, str(ret_))
                                        cl.sendText(to, "Ketik Get-yt {} | angka\nuntuk melihat detail lagu".format(str(search)))
                                if len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["respons"]):
                                        res = data["respons"][num - 1]
                                        with requests.session() as web:
                                            web.headers["User-Agent"] = "Mozilla/5.0"
                                            result = web.get("http://rahandiapi.herokuapp.com/youtubeapi?key=betakey&q=https://www.youtube.com/watch?v={}".format(str(res['video_id'])))
                                            data = result.text
                                            data = json.loads(data)
                                            ret_ = "「 Detail Lagu 」\nTitle : "+data['result']['title']
                                            ret_ += "\nLikes : "+str(data['result']['likes'])
                                            ret_ += "\nDislikes : "+str(data['result']['dislikes'])
                                            ret_ += "\nDuration : "+str(data['result']['duration'])
                                            ret_ += "\nRating : "+str(data['result']['rating'])
                                            ret_ += "\nAuthor : "+str(data['result']['author'])+"\n"
                                            cover = data['result']['thumbnail']
                                            if data["result"]["audiolist"] != []:
                                                for koplok in data["result"]["audiolist"]:
                                                    ret_ += "\nType : "+koplok['extension']
                                                    ret_ += "\nResolusi : "+koplok['resolution']
                                                    ret_ += "\nSize : "+koplok['size']
                                                    ret_ += "\nLink : "+koplok['url']
                                                    if koplok['resolution'] == '50k':
                                                        audio = koplok['url']
                                            cl.sendImageWithURL(msg.to,cover)
                                            cl.sendMessage(msg.to, str(ret_))
                                            cl.sendAudioWithURL(msg.to,audio)
 
                        elif cmd.startswith("get-fs "):
                          if msg._from in admin:
                                sep = msg.text.split(" ")
                                anu = msg.text.replace(sep[0] + " "," ")                
                                with requests.session() as web:
                                    web.headers["user-agent"] = random.choice(settings["userAgent"])
                                    r = web.get("https://farzain.xyz/api/premium/fs.php?apikey=apikey_saintsbot&id={}".format(urllib.parse.quote(anu)))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["status"] == "success":
                                        ret_ = data["url"]
                                        cl.sendImageWithURL(msg.to,ret_)
                                    else:
                                        cl.sendMessage(msg.to, "Error")
                                        
                        elif cmd.startswith("get-post "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            post = msg.text.replace(sep[0] + " ","")
                            with requests.session() as s:
                                s.headers['user-agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                r = s.get("http://m.jancok.com/klik/{}/".format(urllib.parse.quote(post)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                ret_ = '「 Get Postingan 」\n\n'
                                try:
                                    for title in soup.select("[class~=badge-item-title]"):
                                        ret_ += "• Judul : "+title.get_text()
                                        ret_ += "\n• Link : m.jancok.com"
                                    for link in soup.find_all('img',limit=1):
                                        cl.sendMessage(msg.to, ret_)
                                        cl.sendImageWithURL(msg.to, link.get('src'))
                                except Exception as e:
                                    cl.sendMessage(msg.to, "Post kosong")
                                    print(str(e))
                                    
                        elif cmd.startswith("get-line "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            user = text.replace(sep[0] + " ","")
                            conn = cl.findContactsByUserid(user)
                            try:
                                anu = conn.mid
                                dn = conn.displayName
                                bio = conn.statusMessage
                                sendMention(to, anu, "「 Contact Line ID 」\n• Nama : ", "\n• Nick : "+dn+"\n• Bio : "+bio+"\n• Contact link : http://line.me/ti/p/~"+user)
                                cl.sendContact(to, anu)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("invite: "):
                          if msg._from in admin:
                               sep = text.split(" ")
                               idnya = text.replace(sep[0] + " ","")
                               conn = cl.findContactsByUserid(idnya)
                               cl.findAndAddContactsByMid(conn.mid)
                               cl.inviteIntoGroup(msg.to,[conn.mid])
                               group = cl.getGroup(msg.to)
                               xname = cl.getContact(conn.mid)
                               zx = ""
                               zxc = ""
                               zx2 = []
                               xpesan = '「 Sukses Diinvite 」\nNama contact '
                               recky = str(xname.displayName)
                               pesan = ''
                               pesan2 = pesan+"@a\n"
                               xlen = str(len(zxc)+len(xpesan))
                               xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                               zx = {'S':xlen, 'E':xlen2, 'M':xname.mid}
                               zx2.append(zx)
                               zxc += pesan2
                               text = xpesan+ zxc + "ke grup " + str(group.name) +""
                               cl.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd.startswith("youtube"):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                params = {"search_query": search}
                                r = requests.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "╔══[ ʀᴇsᴜʟᴛ ʏᴏᴜᴛᴜʙᴇ ]"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n╠🔷{} ]".format(str(data["title"]))
                                    ret_ += "\n╠🔷 https://www.youtube.com{}".format(str(data["href"]))
                                ret_ += "\n╚══[ ᴛᴏᴛᴀʟ {} ᴠɪᴅᴇᴏ ]".format(len(datas))
                                cl.sendMessage(to, str(ret_))

                        elif cmd.startswith("tr-"):
                                sep = text.split("-")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("tr-" + lang + " ","")
                                if lang not in list_language["list_translate"]:
                                    return ririn.sendMessage(to, "Language not found")
                                translator = Translator()
                                hasil = translator.translate(say, dest=lang)
                                A = hasil.text
                                ririn.sendMessage(to, str(A))

                        elif cmd.startswith("listmeme"):
                          if msg._from in admin:
                            proses = text.split(" ")
                            keyword = text.replace(proses[0] + " ","")
                            count = keyword.split("|")
                            search = str(count[0])
                            r = requests.get("http://api.imgflip.com/get_memes")
                            data = json.loads(r.text)
                            if len(count) == 1:
                                no = 0
                                hasil = "「 Daftar Meme Image 」\n"
                                for aa in data["data"]["memes"]:
                                    no += 1
                                    hasil += "\n" + str(no) + ". "+ str(aa["name"])
                                hasil += " "
                                ret_ = "\n\nSelanjutnya ketik:\nListmeme | angka\nGet-meme text1 | text2 | angka"
                                cl.sendText(msg.to,hasil+ret_)
                            if len(count) == 2:
                                try:
                                    num = int(count[1])
                                    gambar = data["data"]["memes"][num - 1]
                                    hasil = "{}".format(str(gambar["name"]))
                                    sendMention(msg.to, msg._from,"「 Meme Image 」\nTunggu ","\nFoto sedang diproses...")
                                    cl.sendText(msg.to,hasil)
                                    cl.sendImageWithURL(msg.to,gambar["url"])
                                except Exception as e:
                                    cl.sendText(msg.to," "+str(e))
                                    
                        elif cmd.startswith("get-meme "):
                          if msg._from in admin:
                            proses = text.split(" ")
                            keyword = text.replace(proses[0]+" ","")
                            query = keyword.split("|")
                            atas = query[0]
                            bawah = query[1]
                            r = requests.get("https://api.imgflip.com/get_memes")
                            data = json.loads(r.text)
                            try:
                                num = int(query[2])
                                namamem = data["data"]["memes"][num - 1]
                                meme = int(namamem["id"])
                                api = pyimgflip.Imgflip(username='andyihsan', password='ihsan848')
                                result = api.caption_image(meme, atas,bawah)
                                sendMention(msg.to, msg._from,"「 Meme Image 」\nTunggu ","\nFoto sedang diproses...")
                                cl.sendImageWithURL(msg.to,result["url"])
                            except Exception as e:
                                cl.sendText(msg.to," "+str(e))


                        elif cmd.startswith("get-gif "):
                          if msg._from in admin:
                            proses = text.split(" ")
                            urutan = text.replace(proses[0] + " ","")
                            count = urutan.split("|")
                            search = str(count[0])
                            r = requests.get("https://api.tenor.com/v1/search?key=PVS5D2UHR0EV&limit=10&q="+str(search))
                            data = json.loads(r.text)
                            if len(count) == 1:
                                no = 0
                                hasil = "「 Pencarian Gif 」\n"
                                for aa in data["results"]:
                                    no += 1
                                    hasil += "\n" + str(no) + ". " + str(aa["title"])
                                    ret_ = "\n\nSelanjutnya Get-gif {} | angka\nuntuk melihat detail video".format(str(search))
                                cl.sendText(msg.to,hasil+ret_)
                            elif len(count) == 2:
                                try:
                                    num = int(count[1])
                                    b = data["results"][num - 1]
                                    c = str(b["id"])
                                    hasil = "Informasi gif ID "+str(c)
                                    hasil += "\n"
                                    cl.sendText(msg.to,hasil)
                                    dl = str(b["media"][0]["loopedmp4"]["url"])
                                    cl.sendVideoWithURL(msg.to,dl)
                                except Exception as e:
                                    cl.sendText(msg.to," "+str(e))                        
                        
                        elif cmd.startswith("get-xxx "):
                          if msg._from in admin:
                            proses = text.split(" ")
                            urutan = text.replace(proses[0] + " ","")
                            count = urutan.split("|")
                            search = str(count[0])
                            r = requests.get("https://api.avgle.com/v1/search/{}/1?limit=10".format(str(search)))
                            data = json.loads(r.text)
                            if len(count) == 1:
                                no = 0
                                hasil = "「 Pencarian Video 18+ 」\n"
                                for aa in data["response"]["videos"]:
                                    no += 1
                                    hasil += "\n"+str(no)+". "+str(aa["title"])+"\nDurasi : "+str(aa["duration"])
                                    ret_ = "\n\nSelanjutnya Get-xxx {} | angka\nuntuk melihat detail video".format(str(search))
                                cl.sendText(msg.to,hasil+ret_)
                            elif len(count) == 2:
                                try:
                                    num = int(count[1])
                                    b = data["response"]["videos"][num - 1]
                                    c = str(b["vid"])
                                    d = requests.get("https://api.avgle.com/v1/video/"+str(c))
                                    data1 = json.loads(d.text)
                                    hasil = "Judul "+str(data1["response"]["video"]["title"])
                                    hasil += "\n\nDurasi : "+str(data1["response"]["video"]["duration"])
                                    hasil += "\nKualitas HD : "+str(data1["response"]["video"]["hd"])
                                    hasil += "\nDitonton "+str(data1["response"]["video"]["viewnumber"])
                                    e = requests.get("https://api-ssl.bitly.com/v3/shorten?access_token=c52a3ad85f0eeafbb55e680d0fb926a5c4cab823&longUrl="+str(data1["response"]["video"]["video_url"]))
                                    data2 = json.loads(e.text)
                                    hasil += "\nLink video : "+str(data1["response"]["video"]["video_url"])
                                    hasil += "\nLink embed : "+str(data1["response"]["video"]["embedded_url"])
                                    hasil += "\n\nKalau tidak bisa jangan lupa pakai vpn kesayangan anda"
                                    cl.sendText(msg.to,hasil)
                                    anuanu = str(data1["response"]["video"]["preview_url"])
                                    path = cl.downloadFileURL(anuanu)
                                    cl.sendImage(msg.to,path)
                                    cl.sendVideoWithURL(msg.to, data["data"]["url"])
                                except Exception as e:
                                    cl.sendText(msg.to," "+str(e))

                        elif cmd.startswith("get-sholat "):
                          if msg._from in admin:
                             sep = text.split(" ")
                             location = text.replace(sep[0] + " ","")
                             with requests.session() as web:
                                  web.headers["user-agent"] = random.choice(settings["userAgent"])
                                  r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                  data = r.text
                                  data = json.loads(data)
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                         ret_ = "「 Jadwal Sholat 」\n"
                                         ret_ += "\n「⭐」 Lokasi : " + data[0]
                                         ret_ += "\n「⭐」 " + data[1]
                                         ret_ += "\n「⭐」 " + data[2]
                                         ret_ += "\n「⭐」 " + data[3]
                                         ret_ += "\n「⭐」 " + data[4]
                                         ret_ += "\n「⭐」 " + data[5]
                                         ret_ += "\n\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                         ret_ += "\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                  cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("get-cuaca "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            location = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                    ret_ = "「 Status Cuaca 」\n"
                                    ret_ += "\n「✭」 Lokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\n「✭」 Suhu : " + data[1].replace("Suhu : ","") + " C"
                                    ret_ += "\n「✭」 Kelembaban : " + data[2].replace("Kelembaban : ","") + " %"
                                    ret_ += "\n「✭」 Tekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
                                    ret_ += "\n「✭」 Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                    ret_ += "\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("get-lokasi "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "「 Info Lokasi 」"
                                    ret_ += "\n「✭」 Location : " + data[0]
                                    ret_ += "\n「✭」 Google Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                cl.sendMessage(msg.to,str(ret_))

                        elif cmd.startswith("lirik "):
                          if msg._from in admin:
                            data = msg.text.lower().replace("lirik ","")                                
                            artis = data.split('|')
                            artis = artis[1].replace(' ','_')
                            judul = data.split('|')
                            judul = judul[2].replace(' ','_')
                            with requests.session() as s:
                                s.headers['user-agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                r = s.get("https://www.wowkeren.com/lirik/lagu/{}/{}.html".format(urllib.parse.quote(artis), judul))
                                x = s.get("https://www.wowkeren.com/seleb/{}/lirik.html".format(urllib.parse.quote(artis)))
                                data = BeautifulSoup(r.content, 'html5lib')
                                data1 = BeautifulSoup(x.content, 'html5lib')
                                ret_ = ''
                                try:
                                    yyk = data1.select("[class~=content]")[1].text
                                    yoyok = yyk.replace("		", " ")
                                    ret_ += "  「 Informasi Penyanyi 」"+yoyok
                                    ret = data.find("div", id="JudulHalaman")
                                    ret_ += "Judul lagu : "+ret.get_text()
                                    ret_ += "\n\n  「 Lirik Lagunya 」"+data.select("[class~=GambarUtama]")[1].text
                                    for link in data1.findAll('div', attrs={'class':'item'}):
                                        cl.sendImageWithURL(msg.to, "https://www.wowkeren.com"+link.find('img')['src'])
                                    cl.sendMessage(to, ret_)
                                except:
                                    cl.sendMessage(to, "lirik tidak tersedia")

                        elif cmd.startswith("get-lirik "):
                           if msg._from in admin:
                               sep = msg.text.split(" ")
                               search = msg.text.replace(sep[0] + " ","")
                               params = {'songname': search}
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   url = "http://rahandiapi.herokuapp.com/lyricapi?key=betakey&q={}".format(urllib.parse.quote(search))
                                   link = web.get(url)
                                   data = link.text
                                   data = json.loads(data)
                                   start = timeit.timeit()
                                   ret_ = "「 Lirik Search 」"
                                   ret_ += "\n「✭」 Judul : {}".format(str(data["title"]))
                                   ret_ += "\n「✭」 Time Taken : {}".format(str(start))
                                   ret_ += "\n\n{}".format(str(data["lyric"]))
                                   cl.sendText(msg.to, str(ret_))

                        elif cmd.startswith("musik "):
                            if msg._from in admin:
                               sep = msg.text.split(" ")
                               query = msg.text.replace(sep[0] + " ","")
                               cond = query.split("-")
                               search = str(cond[0])
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   result = web.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                   data = result.text
                                   data = json.loads(data)
                                   if len(cond) == 1:
                                      num = 0
                                      ret_ = "「 Pencarian Musik 」\n"
                                      for music in data["result"]:
                                          num += 1
                                          ret_ += "\n {}. {}".format(str(num), str(music["single"]))
                                      ret_ += "\n\n「 Total {} Pencarian 」".format(str(len(data["result"])))
                                      cl.sendMessage(to, str(ret_))
                                      sendMention(msg.to, msg._from,"","\nJika ingin menggunakan,\nSilahkan gunakan:\n\nMusik penyanyi-angka")
                                   if len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(data["result"]):
                                               music = data["result"][num - 1]
                                               with requests.session() as web:
                                                    web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                                    result = web.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                                    data = result.text
                                                    data = json.loads(data)
                                                    if data["result"] != []:
                                                         ret_ = "「 Pencarian Musik 」"
                                                         ret_ += "\n• Judul : {}".format(str(data["result"]["song"]))
                                                         ret_ += "\n• Album : {}".format(str(data["result"]["album"]))
                                                         ret_ += "\n• Ukuran : {}".format(str(data["result"]["size"]))
                                                         ret_ += " \n• Link Musik : {}".format(str(data["result"]["mp3"]))
                                                         ret_ += "\n「 Tunggu Musiknya Keluar 」"
                                                         cl.sendImageWithURL(to, str(data["result"]["img"]))
                                                         cl.sendMessage(to, str(ret_))
                                                         cl.sendAudioWithURL(to, str(data["result"]["mp3"][0]))

                        elif cmd.startswith("kode wilayah"):
                          if msg._from in admin:
                            ret_ = "「 Daftar Kode Wilayah 」\n\n"
                            ret_ += "248 = Alternatif - Cibubur\n119 = Ancol - bandara\n238 = Asia afrika - Bandung\n169 = Asia afrika - Hang lekir"
                            ret_ += "\n276 = Asia afrika - Sudirman\n295 = Bandengan - kota\n294 = Bandengan - Selatan\n255 = Boulevard Barat raya"
                            ret_ += "\n102 = Buncit raya\n272 = Bundaran - HI\n93 = Cideng barat\n289 = Cikini raya\n242 = Ciledug raya - Cipulir"
                            ret_ += "\n175 = Ciloto - Puncak\n142 = Daan mogot - Grogol\n143 = Daan mogot - Pesing\n338 = Dewi sartika - Cawang"
                            ret_ += "\n124 = DI Panjaitan - By pass\n123 = DI Panjaitan - Cawang\n13 = Dr Satrio - Casablanca\n105 = Dr Satrio - Karet"
                            ret_ += "\n245 = Dukuh atas - MRT Jakarta\n334 = Fachrudin raya\n252 = Fatmawati - Blok A\n253 = Fatmawati - Cipete raya"
                            ret_ += "\n203 = Flyover Daan mogot\n336 = Flyover Jati baru\n172 = Flyover Senen - Kramat\n77 = Gunung sahari"
                            ret_ += "\n137 = Hasyim Ashari\n273 = Jalan MH Thamrin\n327 = Jalan RS Fatmawati\n292 = Jl. Otista 3\n333 = Jl. Panjang - Kebon jeruk"
                            ret_ += "\n226 = JORR - Bintaro\n227 = JORR - Fatmawati\n173 = Kramat raya - Senen\n117 = Kyai Caringin - Cideng\n126 = Letjen Suprapto - Senen"
                            ret_ += "\n204 = Mangga besar\n319 = Margaguna raya\n326 = Margonda raya\n310 = Mas Mansyur - Karet\n309 = Mas Mansyur - Tn. Abang"
                            ret_ += "\n64 = Matraman\n140 = Matraman - Salemba\n284 = Metro Pdk. Indah\n191 = MT Haryono - Pancoran\n160 = Pancoran barat"
                            ret_ += "\n331 = Pejompongan - Slipi\n332 = Pejompongan - Sudirman\n312 = Perempatan pramuka\n171 = Permata hijau - Panjang\n99 = Petojo Harmoni"
                            ret_ += "\n223 = Pramuka - Matraman\n222 = Pramuka raya\n314 = Pramuka raya - jl. Tambak\n313 = Pramuka - Salemba raya\n130 = Puncak raya KM84"
                            ret_ += "\n318 = Radio dalam raya\n328 = RS Fatmawati - TB\n274 = Senayan city\n132 = Slipi - Palmerah\n133 = Slipi - Tomang"
                            ret_ += "\n162 = S Parman - Grogol\n324 = Sudirman - Blok M\n18 = Sudirman - Dukuh atas\n325 = Sudirman - Semanggi\n112 = Sudirman - Setiabudi"
                            ret_ += "\n246 = Sudirman - Thamrin\n320 = Sultan agung - Sudirman\n100 = Suryo pranoto\n220 = Tanjung duren\n301 = Tol kebon jeruk"
                            ret_ += "\n41 = Tomang/Simpang\n159 = Tugu Pancoran\n145 = Warung jati - Pejaten\n205 = Yos Sudarso - Cawang\n206 = Yos Sudarso - Tj. Priuk"
                            ret_ += "\n\nUntuk melihat cctv,\nKetik lihat (kode wilayah)"                            
                            cl.sendMessage(to, ret_)

                        elif cmd.startswith("lihat "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            cct = msg.text.replace(sep[0] + " ","")
                            with requests.session() as s:
                                s.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
                                r = s.get("http://lewatmana.com/cam/{}/bundaran-hi/".format(urllib.parse.quote(cct)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                try:
                                    ret_ = "「 Informasi CCTV 」\nDaerah "
                                    ret_ += soup.select("[class~=cam-viewer-title]")[0].text
                                    ret_ += "\nCctv update per 5 menit"
                                    vid = soup.find('source')['src']
                                    ret = "Untuk melihat wilayah lainnya, Ketik kode wilayah"
                                    cl.sendMessage(to, ret_)
                                    cl.sendVideoWithURL(to, vid)
                                    cl.sendMessage(to, ret)
                                except:
                                    cl.sendMessage(to, "Data cctv tidak ditemukan!")

                        elif cmd.startswith("get-image "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            search = msg.text.replace(sep[0] + " ","")
                            url = "http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search))
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["result"] != []:
                                    start = timeit.timeit()
                                    items = data["result"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    cl.sendText(msg.to,"「 Google Image 」\nType : Search Image\nTime taken : %seconds" % (start))
                                    cl.sendImageWithURL(msg.to, str(path))

                        elif cmd.startswith("get-apk "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            query = msg.text.replace(sep[0] + " ","")
                            cond = query.split("|")
                            search = str(cond[0])
                            with requests.session() as s:
                                s.headers['user-agent'] = random.choice(settings["userAgent"])
                                r = s.get("https://apkpure.com/id/search?q={}".format(str(search)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                data = soup.findAll('dl', attrs={'class':'search-dl'})
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "「 Pencarian Aplikasi 」\n"
                                    for apk in data:
                                        num += 1
                                        link = "https://apkpure.com"+apk.find('a')['href']
                                        title = apk.find('a')['title']
                                        ret_ += "\n {}. {}".format(str(num), str(title))
                                    ret_ += "\n\n Total {} Result".format(str(len(data)))
                                    ret = "Selanjutnya ketik:\nGet-apk {} | angka".format(str(search))
                                    cl.sendMessage(to, str(ret_))
                                    cl.sendMessage(to, str(ret))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data):
                                        apk = data[num - 1]
                                        with requests.session() as s:
                                            s.headers['user-agent'] = random.choice(settings["userAgent"])
                                            r = s.get("https://apkpure.com{}/download?from=details".format(str(apk.find('a')['href'])))
                                            soup = BeautifulSoup(r.content, 'html5lib')
                                            data = soup.findAll('div', attrs={'class':'fast-download-box'})
                                            for down in data:
                                                load = down.select("a[href*=https://download.apkpure.com/]")[0]
                                                file = load['href']
                                                ret_ = "File info :\n"+down.find('span', attrs={'class':'file'}).text
                                                with requests.session() as web:
                                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                                    r = web.get("https://api-ssl.bitly.com/v3/shorten?access_token=497e74afd44780116ed281ea35c7317285694bf1&longUrl={}".format(urllib.parse.quote(file)))
                                                    data = r.text
                                                    data = json.loads(data)
                                                    ret_ += "\nLink Download :\n"+data["data"]["url"]
                                                cl.sendMessage(to, str(ret_))

                        elif cmd.startswith("get-anime "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            anime = msg.text.replace(sep[0] + " ","%20")                
                            with requests.session() as web:
                                web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                            r = web.get("https://kitsu.io/api/edge/anime?filter[text]={}".format(urllib.parse.quote(anime)))
                            data = r.text
                            data = json.loads(data)
                            ret_ = ''
                            if data["data"] != []:
                                for a in data["data"]:
                                    if a["attributes"]["subtype"] == "TV":
                                        sin = a["attributes"]["synopsis"]
                                        translator = Translator()
                                        hasil = translator.translate(sin, dest='id')
                                        sinop = hasil.text
                                        ret_ += '「 Anime {} 」'.format(str(a["attributes"]["canonicalTitle"]))
                                        ret_ += '\n• Rilis : '+str(a["attributes"]["startDate"])
                                        ret_ += '\n• Rating : '+str(a["attributes"]["ratingRank"])
                                        ret_ += '\n• Type : '+str(a["attributes"]["subtype"])
                                        ret_ += '\n• Sinopsis :\n'+str(sinop)
                                        ret_ += '\n\n'
                                        cl.sendImageWithURL(msg.to, str(a["attributes"]["posterImage"]["small"]))
                            cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("get-zodiak "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            query = text.replace(sep[0] + " ","")
                            r = requests.post("https://aztro.herokuapp.com/?sign={}&day=today".format(urllib.parse.quote(query)))
                            data = r.text
                            data = json.loads(data)
                            data1 = data["description"]
                            data2 = data["color"]
                            translator = Translator()
                            hasil = translator.translate(data1, dest='id')
                            hasil1 = translator.translate(data2, dest='id')
                            A = hasil.text
                            B = hasil1.text
                            ret_ = "「 Ramalan zodiak {} hari ini 」\n".format(str(query))
                            ret_ += str(A)
                            ret_ += "\n======================\n• Tanggal : " +str(data["current_date"])
                            ret_ += "\n• Rasi bintang : "+query
                            ret_ += " ("+str(data["date_range"]+")")
                            ret_ += "\n• Pasangan Zodiak : " +str(data["compatibility"])
                            ret_ += "\n• Angka keberuntungan : " +str(data["lucky_number"])
                            ret_ += "\n• Waktu keberuntungan : " +str(data["lucky_time"])
                            ret_ += "\n• Warna kesukaan : " +str(B)
                            cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("get-bintang "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            url = msg.text.replace(sep[0] + " ","")    
                            with requests.session() as s:
                                s.headers['user-agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                r = s.get("https://www.vemale.com/zodiak/{}".format(urllib.parse.quote(url)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                ret_ = ""
                                for a in soup.select('div.vml-zodiak-detail'):
                                    ret_ += a.h1.string
                                    ret_ += "\n"+ a.h4.string
                                    ret_ += " : "+ a.span.string +""
                                for b in soup.select('div.col-center'):
                                    ret_ += "\nTanggal : "+ b.string
                                for d in soup.select('div.number-zodiak'):
                                    ret_ += "\nAngka keberuntungan : "+ d.string
                                for c in soup.select('div.paragraph-left'):
                                    ta = c.text
                                    tab = ta.replace("    ", "")
                                    tabs = tab.replace(".", ".\n")
                                    ret_ += "\n"+ tabs
                                    #print (ret_)
                                cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("get-telpon "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            nomor = text.replace(sep[0] + " ","")
                            r = requests.get("http://apisora2.herokuapp.com/prank/call/?no={}".format(urllib.parse.quote(nomor)))
                            data = r.text
                            data = json.loads(data)
                            ret_ = "「 Prangked Telpon 」"
                            ret_ += "\n• Status : {}".format(str(data["status"]))
                            ret_ += "\n• Tujuan "+str(data["result"])
                            cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("get-sms "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            nomor = text.replace(sep[0] + " ","")
                            r = requests.get("http://apisora2.herokuapp.com/prank/sms/?no={}".format(urllib.parse.quote(nomor)))
                            data = r.text
                            data = json.loads(data)
                            ret_ = "「 Prangked Sms 」"
                            ret_ += "\n• Status : {}".format(str(data["status"]))
                            ret_ += "\n• Tujuan "+str(data["result"])
                            cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("get-mimpi "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            mimpi = msg.text.replace(sep[0] + " ","")  
                            with requests.session() as s:
                                s.headers['user-agent'] = 'Mozilla/5.0'
                                r = s.get("http://primbon.com/tafsir_mimpi.php?mimpi={}&submit=+Submit+".format(urllib.parse.quote(mimpi)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                for anu in soup.find_all('i'):
                                    ret_ = anu.get_text()
                                    cl.sendMessage(msg.to,ret_)

                        elif text.lower() == 'top kaskus':
                           if msg._from in admin:
                               r = requests.get("https://api.bayyu.net/kaskus-hotthread/?apikey=c28c944199384f191335f1f8924414fa839350d&page=2")
                               data=r.text
                               data=json.loads(data)                                                                                                      
                               if data["hot_threads"] != []:
                                   no = 0
                                   hasil = "「 Kaskus Search 」\n"
                                   for news in data["hot_threads"]:
                                        no += 1                  
                                        hasil += "\n" + str(no) + ". Judul : " + str(news["title"]) + "\n • Deskripsi : " + str(news["detail"]) + "\n• Link: " + str(news["link"]) + "\n"
                                        hasil += "\n"
                                   cl.sendText(msg.to, str(hasil))

                        elif cmd.startswith("get-video "):
                          if msg._from in admin:
                                sep = msg.text.split(" ")
                                search = msg.text.replace(sep[0] + " ","")
                                with requests.session() as web:
                                      web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                      url = web.get("http://rahandiapi.herokuapp.com/youtubeapi/search?key=betakey&q={}".format(urllib.parse.quote(search)))
                                      data = url.text
                                      data = json.loads(data)
                                      if data["result"] != []:
                                          video = random.choice(data["result"]["videolist"])
                                          vid = video["url"]
                                          start = timeit.timeit()
                                          ret = "「 Informasi Video 」\n"
                                          ret += "• Judul : {}".format(str(data["result"]["title"]))
                                          ret += "\n• Author : {}".format(str(data["result"]["author"]))
                                          ret += "\n• Durasi : {}".format(str(data["result"]["duration"]))
                                          ret += "\n• Like nya : {}".format(str(data["result"]["likes"]))
                                          ret += "\n• Rating : {}".format(str(data["result"]["rating"]))
                                          ret += "\n• TimeTaken : {}".format(str(start))
                                          ret += "\n• Deskripsi : {}\n「 Waiting Encoding 」".format(str(data["result"]["description"]))
                                          cl.sendText(msg.to, str(ret))
                                          cl.sendVideoWithURL(msg.to, str(vid))

                        elif cmd.startswith("get-mp3 "):
                          if msg._from in admin:
                                sep = msg.text.split(" ")
                                search = msg.text.replace(sep[0] + " ","")
                                with requests.session() as web:
                                      web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                      url = web.get("http://rahandiapi.herokuapp.com/youtubeapi/search?key=betakey&q={}".format(urllib.parse.quote(search)))
                                      data = url.text
                                      data = json.loads(data)
                                      if data["result"] != []:
                                          audio = random.choice(data["result"]["audiolist"])
                                          aud = audio["url"]
                                          start = timeit.timeit()
                                          ret = "「 Informasi Mp3 」\n"
                                          ret += "• Judul : {}".format(str(data["result"]["title"]))
                                          ret += "\n• Author : {}".format(str(data["result"]["author"]))
                                          ret += "\n• Durasi : {}".format(str(data["result"]["duration"]))
                                          ret += "\n• Like nya : {}".format(str(data["result"]["likes"]))
                                          ret += "\n• Rating : {}".format(str(data["result"]["rating"]))
                                          ret += "\n• TimeTaken : {}".format(str(start))
                                          ret += "\n• Deskripsi : {}\n「 Waiting Encoding 」".format(str(data["result"]["description"]))
                                          cl.sendText(msg.to, str(ret))
                                          cl.sendAudioWithURL(msg.to, str(aud))

                        elif cmd.startswith("get-instagram "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                                data = response.json()
                                namaIG = str(data['graphql']['user']['full_name'])
                                bioIG = str(data['graphql']['user']['biography'])
                                mediaIG = str(data['graphql']['user']['edge_owner_to_timeline_media']['count'])
                                verifIG = str(data['graphql']['user']['is_verified'])
                                usernameIG = str(data['graphql']['user']['username'])
                                followerIG = str(data['graphql']['user']['edge_followed_by']['count'])
                                profileIG = data['graphql']['user']['profile_pic_url_hd']
                                privateIG = str(data['graphql']['user']['is_private'])
                                followIG = str(data['graphql']['user']['edge_follow']['count'])
                                link = "• Link : " + "https://www.instagram.com/" + instagram
                                text = "「 Instagram User 」\n• Name : "+namaIG+"\n• Username : "+usernameIG+"\n• Follower : "+followerIG+"\n• Following : "+followIG+"\n• Total post : "+mediaIG+"\n• Verified : "+verifIG+"\n• Private : "+privateIG+"\n• Biography : "+bioIG+"" "\n" + link
                                cl.sendImageWithURL(msg.to, profileIG)
                                cl.sendMessage(msg.to, str(text))
                            except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("cekdate "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            cl.sendMessage(msg.to,"「 Date Info 」\n"+"「✭」 Date Of Birth : "+lahir+"\n「✭」 Age : "+usia+"\n「✭」 Ultah : "+ultah+"\n「✭」 Zodiak : "+zodiak)

                        elif cmd.startswith("spamtag: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["RAlimit"] = num
                                cl.sendText(msg.to,"「 Status Spamtag 」\nBerhasil diubah jadi {} kali".format(str(strnum)))

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendText(msg.to,"「 Status Spamcall 」\nBerhasil diubah jadi {} kali".format(str(strnum)))

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["RAlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))
                                    else:
                                        cl.sendText(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd.startswith("panggil "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(key1)
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))

                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                cl.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                call.acquireGroupCallRoute(to)
                                call.inviteIntoGroupCall(to, contactIds=members)
                                        
                        elif cmd.startswith("spamcall "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                proses = text.split(" ")
                                strnum = text.replace(proses[0] + " ","")
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jumlah = int(strnum)
                                cl.sendText(msg.to,"Undangan call grup {} sukses".format(str(strnum)))
                                if jumlah <= 1000:
                                   for x in range(jumlah):
                                   	try:
                                           call.acquireGroupCallRoute(to)
                                           call.inviteIntoGroupCall(to, contactIds=members)
                                   	except Exception as e:
                                          cl.sendText(msg.to,str(e))

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              cl.sendText(msg.to,"「 Spam Gift 」\nBerhasil spamgift {} kali".format(str(jumlah)))
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      
                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["RAmessage1"]))

                        elif cmd == "trbot" or cmd == "trbots":
                          if wait["selfbott"] == True:
                            if msg._from in admin:
                                cl.sendMessage(msg.to, "тeaм")
                                ki.sendMessage(msg.to, "тeaм ")
                                kk.sendMessage(msg.to, "тeaм")
                                kc.sendMessage(msg.to, "тeaм")
                                kb.sendMessage(msg.to, "тeaм")
                                kd.sendMessage(msg.to, "тeaм")
                                ke.sendMessage(msg.to, "тeaм")
                                kf.sendMessage(msg.to, "тeaм")
                                kj.sendMessage(msg.to, "тeaм")
                                sw.sendMessage(msg.to, "тeaм")
                                cl.sendMessage(msg.to, "тeaм all ready\nAmankan Room\nDemi Amanatnya Bos ")
                                

                        elif cmd == "invite bot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid]
                                    cl.inviteIntoGroup(msg.to, anggota)
                                    ki.acceptGroupInvitation(msg.to)
                                    kk.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    kb.acceptGroupInvitation(msg.to)
                                    kd.acceptGroupInvitation(msg.to)
                                    ke.acceptGroupInvitation(msg.to)
                                    kf.acceptGroupInvitation(msg.to)
                                    kg.acceptGroupInvitation(msg.to)
                                    kh.acceptGroupInvitation(msg.to)
                                    cl.sendMessage(msg.to,"Grup "+str(ginfo.name)+"ᴍᴀsɪʜ ᴛᴇʀᴋᴇɴᴅᴀʟɪ ʙᴏss")
                                except:
                                    pass
                                    
                        elif cmd == "stay":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, [Jmid,Zmid])
                                    cl.sendMessage(msg.to,"Grup "+str(ginfo.name)+"sᴛᴀʏ ᴅɪ ʟᴜᴀʀ ʙᴏss")
                                except:
                                    pass           

                        elif cmd == "join":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                #cl.sendMessage(msg.to, "↪ᴘᴇʀᴋᴇɴᴀʟᴋᴀɴ ᴛᴇᴀᴍ ᴛᴇʀxʙᴏᴛs ʜᴀᴅɪʀ ᴅɪ ↩"+str(G.name))
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)                        
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)              
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)                         
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)                          
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)

                        elif cmd == "bye":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ki.sendMessage(msg.to, "ɢᴏᴏᴅ ʙʏᴇ "+str(G.name))
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                kb.leaveGroup(msg.to)
                                kd.leaveGroup(msg.to)
                                ke.leaveGroup(msg.to)
                                kf.leaveGroup(msg.to)
                                
                        elif cmd == "!bye":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.sendMessage(msg.to, "Asalamu.alaikum..wr..wb..! ʙʏᴇ ʙʏᴇ "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd.startswith("leave "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        ki.sendMessage(i, "Silahkan admin invite atau masukan kembali")
                                        ki.leaveGroup(i)
                                        kk.leaveGroup(i)
                                        kc.leaveGroup(i)
                                        kb.leaveGroup(i)
                                        cl.sendMessage(to,"Berhasil keluar dari grup " +h)

                        elif cmd == "Terx1":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)

                        elif cmd == "Terx2":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kk.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kk.updateGroup(G)

                        elif cmd == "Terx3":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)
                                
                        elif cmd == "Terx4":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kb.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kb.updateGroup(G) 
        
                        elif cmd == "Terx5":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kd.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kd.updateGroup(G)

                        elif cmd == "Terx6":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ke.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ke.updateGroup(G)

                        elif cmd == "Terx7":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kf.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kf.updateGroup(G)
                                
                        elif cmd == "Terx8":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kj.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kj.updateGroup(G) 
                                
                        elif cmd == "Terx9":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kh.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)        
 
                        elif cmd == "jin":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kj.sendMessage(msg.to, "ᴛᴇʀx-ʙᴏᴛs "+str(G.name))
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                sw.sendMessage(msg.to, "ᴛᴇʀx-ʙᴏᴛs "+str(G.name))
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "jut":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                kj.sendMessage(msg.to, " ᴛᴇʀx -ʙᴏᴛs "+str(G.name))
                                kj.leaveGroup(msg.to)
                                sw.sendMessage(msg.to, " ᴛᴇʀx-ʙᴏᴛs"+str(G.name))
                                sw.leaveGroup(msg.to)

                        elif ("Nk " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           sw.kickoutFromGroup(msg.to, [target])
                                           sw.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass

                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           cl.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴀᴅᴍɪɴ")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           cl.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ sᴛᴀғғ")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           admin.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           staff.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "admin:repeat" or text.lower() == 'admin:repeat':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "staff:repeat" or text.lower() == 'staff:repeat':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "bot:repeat" or text.lower() == 'bot:repeat':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                cl.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴅɪ ʀᴇғʀᴇsʜ ʙᴏss...")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "mybot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                cl.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                cl.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "talkban on" or text.lower() == 'talkban on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["talkban"] = True
                                cl.sendMessage(msg.to,"Talk Ban diaktifkan")

                        elif cmd == "talkban off" or text.lower() == 'talkban off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["talkban"] = False
                                cl.sendMessage(msg.to,"Talk Ban dinonaktifkan")

                        elif cmd == "bl" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    cl.sendMessage(msg.to,"✅вacĸlιѕт clear")
                                    ki.sendMessage(msg.to,"✅вacĸlιѕт clear")
                                    kk.sendMessage(msg.to,"✅вacĸlιѕт clear")
                                    kc.sendMessage(msg.to,"✅вacĸlιѕт clear")
                                    kb.sendMessage(msg.to,"✅вacĸlιѕт clear")
                                    kd.sendMessage(msg.to,"✅вacĸlιѕт clear")
                                    ke.sendMessage(msg.to,"✅вacĸlιѕт clear")
                                    kf.sendMessage(msg.to,"✅вacĸlιѕт clear")
                                    kj.sendMessage(msg.to,"✅вacĸlιѕт clear")
                                    sw.sendMessage(msg.to,"✅вacĸlιѕт clear")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "cban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              cl.sendMessage(msg.to,"ѕυcceѕѕ clearιng☑ " +mc)
                              ki.sendMessage(msg.to,"ѕυcceѕѕ clearιng☑ " +mc)
                              kk.sendMessage(msg.to,"ѕυcceѕѕ clearιng☑ " +mc)
                              kc.sendMessage(msg.to,"ѕυcceѕѕ clearιng☑ " +mc)
                              kb.sendMessage(msg.to,"ѕυcceѕѕ clearιng☑ " +mc)
                              kd.sendMessage(msg.to,"ѕυcceѕѕ clearιng☑ " +mc)
                              ke.sendMessage(msg.to,"ѕυcceѕѕ clearιng☑ " +mc)
                              kf.sendMessage(msg.to,"ѕυcceѕѕ clearιng☑ " +mc)
                              kj.sendMessage(msg.to,"ѕυcceѕѕ clearιng☑ " +mc)
                              sw.sendMessage(msg.to,"ѕυcceѕѕ clearιng☑ " +mc)

                        elif 'Ajs ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ajs ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "Anti JS sudah aktif"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "✅Anti JS Diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "🎴Anti JS Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Anti JS Sudah Tidak Aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'Ghost ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ghost ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "Ghost sudah aktif"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "✅Ghost Diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "🎴Ghost Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Ghost Sudah Tidak Aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
#=========== [ Add Image ] ============#
                        elif cmd.startswith("addimg "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in images:
                                wait["Addimage"]["status"] = True
                                wait["Addimage"]["name"] = str(name.lower())
                                images[str(name.lower())] = ""
                                f = codecs.open("image.json","w","utf-8")
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Silahkan kirim fotonya...") 
                            else:
                                cl.sendText(msg.to, "Foto itu sudah dalam list") 
                                
                        elif cmd.startswith("dellimg "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in images:
                                cl.deleteFile(images[str(name.lower())])
                                del images[str(name.lower())]
                                f = codecs.open("image.json","w","utf-8")
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Berhasil menghapus {}".format( str(name.lower())))
                            else:
                                cl.sendText(msg.to, "Foto itu tidak ada dalam list") 
                                 
                        elif text.lower() == "listimage":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 Daftar Image 」\n\n"
                             for image in images:
                                 no += 1
                                 ret_ += str(no) + ". " + image.title() + "\n"
                             ret_ += "\nTotal「{}」Images".format(str(len(images)))
                             cl.sendText(to, ret_)
#=========== [ Add Video ] ============#                               
                        elif cmd.startswith("addvideo "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in videos:
                                wait["Addvideo"]["status"] = True
                                wait["Addvideo"]["name"] = str(name.lower())
                                videos[str(name.lower())] = ""
                                f = codecs.open("video.json","w","utf-8")
                                json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Silahkan kirim videonya...") 
                            else:
                                cl.sendText(msg.to, "Video itu sudah dalam list") 
                                
                        elif cmd.startswith("dellvideo "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in videos:
                                cl.deleteFile(videos[str(name.lower())])
                                del videos[str(name.lower())]
                                f = codecs.open("video.json","w","utf-8")
                                json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Berhasil menghapus video {}".format( str(name.lower())))
                            else:
                                cl.sendText(msg.to, "Video itu tidak ada dalam list") 
                                 
                        elif text.lower() == "listvideo":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 Daftar Video 」\n\n"
                             for video in videos:
                                 no += 1
                                 ret_ += str(no) + ". " + video.title() + "\n"
                             ret_ += "\nTotal「{}」Videos".format(str(len(videos)))
                             cl.sendText(to, ret_)
                             sendMention(msg.to, msg._from,"","\nJika ingin play video nya,\nSilahkan ketik nama - judul\nBisa juga ketik namanya saja")
#=========== [ Add Video ] ============#                               
                        elif cmd.startswith("addmp3 "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in audios:
                                wait["Addaudio"]["status"] = True
                                wait["Addaudio"]["name"] = str(name.lower())
                                audios[str(name.lower())] = ""
                                f = codecs.open("audio.json","w","utf-8")
                                json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Silahkan kirim mp3 nya...") 
                            else:
                                cl.sendText(msg.to, "Mp3 itu sudah dalam list") 
                                
                        elif cmd.startswith("dellmp3 "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in audios:
                                cl.deleteFile(audios[str(name.lower())])
                                del audios[str(name.lower())]
                                f = codecs.open("audio.json","w","utf-8")
                                json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Berhasil menghapus mp3 {}".format( str(name.lower())))
                            else:
                                cl.sendText(msg.to, "Mp3 itu tidak ada dalam list") 
                                 
                        elif cmd == "listmp3":
                             no = 0
                             ret_ = "「 Daftar Lagu 」\n\n"
                             for audio in audios:
                                 no += 1
                                 ret_ += str(no) + ". " + audio.title() + "\n"
                             ret_ += "\nTotal「{}」Lagu".format(str(len(audios)))
                             cl.sendText(to, ret_)
                             sendMention(msg.to, msg._from,"","\nJika ingin play mp3 nya,\nSilahkan ketik nama - judul\nBisa juga ketik namanya saja")
#=========== [ Add Sticker ] ============#                                            
                        elif cmd.startswith("addsticker "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in stickers:
                                wait["Addsticker"]["status"] = True
                                wait["Addsticker"]["name"] = str(name.lower())
                                stickers[str(name.lower())] = ""
                                f = codecs.open("sticker.json","w","utf-8")
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Silahkan kirim stickernya...") 
                            else:
                                cl.sendText(msg.to, "Sticker itu sudah dalam list") 
                                
                        elif cmd.startswith("dellsticker "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in stickers:
                                del stickers[str(name.lower())]
                                f = codecs.open("sticker.json","w","utf-8")
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Berhasil menghapus sticker {}".format( str(name.lower())))
                            else:
                                cl.sendText(msg.to, "Sticker itu tidak ada dalam list") 
                                 
                        elif text.lower() == "liststicker":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 Daftar Sticker 」\n\n"
                             for sticker in stickers:
                                 no += 1
                                 ret_ += str(no) + ". " + sticker.title() + "\n"
                             ret_ += "\nTotal「{}」Stickers".format(str(len(stickers)))
                             cl.sendText(to, ret_)
                             
                        elif cmd == "promo":
                          if msg._from in admin:
                             cl.sendMessage(msg.to,"──────┅☆͜͡┅──────\nᴼᴾᴱᴺ ᴼᴿᴰᴱᴿ\n────────┅┅───────\n➣ꜱᴇʟꜰʙᴏᴛ ᴏɴʟʏ\n➣ꜱᴇʟꜰʙᴏᴛ + ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 2 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 3 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 4 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 5 ᴀꜱɪꜱᴛ\n➣ʙᴏᴛᴘʀᴏᴛᴇᴄᴛ 3-11 ʙᴏᴛ ᴀꜱɪꜱᴛ\n─────────┅┅─────────\n  ✯C͜͡r͜͡e͜͡a͜͡t͜͡o͜͡r✯͜͡$͜͡ë͜͡I͜͡F͜͡-͜͡฿͜͜͡͡o͜͡t͜͡ ͜͡✯\nline.me/ti/p/~gerhanaselatan\nline.me/ti/p/~cyberline11\n➣ѕєʟғвот κɪcκєʀ_+_ᴘʀᴏᴛᴇᴄᴛ\n────────┅͜͡☆͜͡┅────────")
                             msg.contentType = 13
                             msg.contentMetadata = {'mid': admin}
                             tanya = msg.text.replace("promo ","")
                             jawab = ("──────┅☆͜͡┅──────\nᴼᴾᴱᴺ ᴼᴿᴰᴱᴿ\n────────┅┅───────\n➣ꜱᴇʟꜰʙᴏᴛ ᴏɴʟʏ\n➣ꜱᴇʟꜰʙᴏᴛ + ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 2 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 3 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 4 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 5 ᴀꜱɪꜱᴛ\n➣ʙᴏᴛᴘʀᴏᴛᴇᴄᴛ 3-11 ʙᴏᴛ ᴀꜱɪꜱᴛ\n─────────┅┅─────────\n  ✯C͜͡r͜͡e͜͡a͜͡t͜͡o͜͡r✯͜͡$͜͡ë͜͡I͜͡F͜͡-͜͡฿͜͜͡͡o͜͡t͜͡ ͜͡✯\nline.me/ti/p/~gerhanaselatan\nline.me/ti/p/~cyberline\n➣ѕєʟғвот κɪcκєʀ_+_ᴘʀᴏᴛᴇᴄᴛ\n────────┅☆͜͡┅────────")
                             jawaban = random.choice(jawab)
                             tts = gTTS(text=jawaban, lang='id')
                             tts.save('tts.mp3')
                             cl.sendAudio(msg.to,'tts.mp3')
                             cl.sendMessage(msg)         
                             cl.sendMessage(msg.to,"Jika Berminat Langsung Hubungi Kami Ya Trima Kasih😊😊")

                        elif cmd == "terxkibar":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendContact(to, mid)
                               cl.sendMessage(msg.to, "█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
 "ASSALAMUALAIKUM\n"
"  ╭━TEAM TERX-BOTS-SADIS\n"
"  ╰╮┏━┳┳┓┏┳┳┓┏┳┳┳┓\n"
"  ┏┻╋━┻┻┫┣┻┻┫┣┻┻┻┫\n"
"  ┃HAI▪┃KMI DTANG LGI┃\n"
"  ┗ⓞⓞ┻┻ⓞ━━ⓞ┻┻ⓞ━╯\n"
"UNTUK MEMBAKAR\nROOM KALIAN\n"
"..  (҂`_´)\n"
   " <,︻╦̵̵̿╤━ ҉     ~  •"
"█۞███████]▄▄▄▄▄▄▃●●\n"
"▂▄▅█████████▅▄▃▂…"
"[██████████████████]\n"
"◥⊙⊙▲⊙▲⊙▲⊙▲⊙▲⊙\n"
"╭━╮╭━╮\n"
"┃┃╰╯┃┃\n"
"┃╭╮╭╮┣┳━╮╭━━┳━━┳┳━╮\n"
"┃┃┃┃┃┣┫╭╮┫╭╮┃╭╮┣┫╭╯\n"
"┃┃┃┃┃┃┃┃┃┃╰╯┃╰╯┃┃┃\n"
"╰╯╰╯╰┻┻╯╰┻━╮┣━╮┣┻╯\n"
"╱╱╱╱╱╱╱╱╱╭━╯┣━╯┃\n"
"╱╱╱╱╱╱╱╱╱╰━━┻━━╯\n"
"TANPA BANYAK NGEMENG\n"
"GUE SITA ROOM KALIAN\n" 
"JANGAN NANGIS JANGAN MLONGO\n"
"AYO TANGKIS KLO MAMPU\n"
"TEAM TERX-BOTS-SADIS\n"
"━━━━━━━━━━━━━\n"
	"GAK PERNAH BIKIN ULAH\n"
	"MAKA KALI INI MARAH\n"
	"TERX-BOTS-SADIS NGAMUK\n"
	"TANGKIS KLO KLIAN MAMPU\n"
"━━━━━━━━━━━━━\n"
	"TEAM TERX-BOTS-SADIS\n"
	"***SADIS KILER***\n" 
	"TAR-TER-TAR-TOR\n"
	"╚══╝         ╚╩╝\n"
"━━━━━━━━━━━━━\n"        
"JANGAN SOK LO YA AMA TEAM KAMI\n"
"JANGAN SOK LO YA AMA TEAM KAMI\n"
"TEAM TERX-BOTS-SADIS\n"
		"╔═╗╔══╗╔══╗╔══╗\n"
		"║╬║║╔╗║╚╗╔╝║╔╗║\n"
		"║╗╣║╠╣║━║║━║╠╣║\n"
		"╚╩╝╚╝╚╝━╚╝━╚╝╚╝\n"
		"━━━━━━━━━━━━━━━\n"
		"╔═╗╔══╗╔══╗╔══╗\n"
		"║╬║║╔╗║╚╗╔╝║╔╗║\n"
		"║╗╣║╠╣║━║║━║╠╣║\n"
		"╚╩╝╚╝╚╝━╚╝━╚╝╚╝\n"
		"━━━━━━━━━━━━━━━\n"
		"╔═╗╔══╗╔══╗╔══╗\n"
		"║╬║║╔╗║╚╗╔╝║╔╗║\n"
		"║╗╣║╠╣║━║║━║╠╣║\n"
		"╚╩╝╚╝╚╝━╚╝━╚╝╚╝\n"
		"━━━━━━━━━━━━━━━\n"
">>>lain x jangan sok songong ama kami>><\ningat  yee,,klo lu dendam cari kami\n<<<<<<<<<>>\nhttp://line.me/ti/p/~gerhanaselatan\nhttp://line.me/ti/p/~cyberline11")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"15996978","STKPKGID":"1416471","STKVER":"1"}, contentType=7)

                        elif cmd == "trbot" or cmd == "trbots":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               cl.sendMessage(msg.to, "[ᴛᴇʀx-ʙᴏᴛs")
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "╚sᴛᴀʏ\n╚ʙᴏss╗".format(str(elapsed_time)))

                        elif cmd == "harga":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "╭══════════\n║─[     DAFTAR HARGA     ]─ \n║SELFBOT ONLY = 75K /BLN\n║2 ASSIST = 100K /BLN\n║5 ASSIST = 200K /BLN\n║10 ASSIST = 300K /BLN\n║\n║PROTECT ANTIJS\n║\n║2 BOT + ANTIJS = 150K /BLN\n║5 BOT + ANTIJS = 300K /BLN\n║10 BOT + ANTIJS = 400K /BLN\n║\n║═ই\═ANDA BERMINAT\n║ SILAHKAN ADD CONTACT \n║ DIBAWAH INI   \n║\n║http://line.me/ti/p/~gerhanadelatan\n║       MAKASIH      \n║\n╰════════════")
                               cl.sendMessage(msg.to, "Yuk yang minat di Order.... ")
#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Welcome 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Welcome 」\n" + msgs)

                        elif 'Protecturl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protecturl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect Url 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect Url 」\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect kick 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect kick 」\n" + msgs)

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect Join 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect Join 」\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect Cancel 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect Cancel 」\n" + msgs)

                        elif 'Protectinvite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect Invite 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect Invite 」\n" + msgs)

                        elif 'Allpro ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Allpro ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                      msgs += "\nSemua sudah diaktifkan"
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                      msgs += "\nSemua protection diaktifkan"
                                  cl.sendMessage(msg.to, "「 Status Protection 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                         msgs += "\nSemua protection dimatikan"
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                         msgs += "\nSemua protection dimatikan"
                                    cl.sendMessage(msg.to, "「 Status Protection 」\n" + msgs)

#===========COMMAND ON OFF============#
                        elif cmd == "spaminvite on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["SpamInvite"] = True
                                cl.sendMessage(msg.to,"Send Contact to spam grup..")

                        elif cmd == "spaminvite off":
                          if wait["selfbot"] == False:
                            if msg._from in admin:
                                settings["SpamInvite"] = False
                                cl.sendMessage(msg.to,"Send Contact to send grup Off..")

                        elif cmd == "unsend on" or text.lower() == 'unsend on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["unsend"] = True
                                sendMention(msg.to, sender, "「 Status Unsend 」\nUser ", "\nSilahkan unsend pesannya,\nKetik unsend off jika sudah slesai")

                        elif cmd == "unsend off" or text.lower() == 'unsend off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["unsend"] = False
                                sendMention(msg.to, sender, "「 Status Unsend 」\nUser ", " \nDeteksi unsend dinonaktifkan")

                        elif cmd == "timeline on" or text.lower() == 'timeline on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = True
                                sendMention(msg.to, sender, "「 Status Timeline 」\nUser ", "\nSilahkan kirim postingannya,\nKetik timeline off jika sudah slesai")

                        elif cmd == "timeline off" or text.lower() == 'timeline off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = False
                                sendMention(msg.to, sender, "「 Status Timeline 」\nUser ", " \nDeteksi timeline dinonaktifkan")
                                
                        elif cmd == "invite on" or text.lower() == 'invite on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = True
                                sendMention(msg.to, sender, "「 Status Invite 」\nUser ", "\nSilahkan kirim kontaknya,\nKetik invite off jika sudah slesai")

                        elif cmd == "invite off" or text.lower() == 'invite off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = False
                                sendMention(msg.to, sender, "「 Status Invite 」\nUser ", " \nInvite via contact dinonaktifkan")
                                
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["mentionKick"] = True
                                cl.sendText(msg.to,"「 Status Notag 」\nNotag telah diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["mentionKick"] = False
                                cl.sendText(msg.to,"「 Status Notag 」\nNotag telah dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                sendMention(msg.to, sender, "「 Status Contact 」\nUser ", "\nSilahkan kirim kontaknya,\nJika sudah selesai, ketik contact off")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                cl.sendText(msg.to,"「 Status Contact 」\nDeteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                cl.sendText(msg.to,"「 Status Respon 」\nAuto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                cl.sendText(msg.to,"「 Status Respon 」\nAuto respon dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                cl.sendText(msg.to,"「 Status Autojoin 」\nAutojoin telah diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                cl.sendText(msg.to,"「 Status Autojoin 」\nAutojoin telah dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                cl.sendText(msg.to,"「 Status Autoleave 」\nAutoleave telah diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                cl.sendText(msg.to,"「 Status Autoleave 」\nAutoleave telah dinonaktifkan")

                        elif cmd == "autoblock on" or text.lower() == 'autoblock on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = True
                                cl.sendText(msg.to,"「 Status Autoleave 」\nAutoleave telah diaktifkan")

                        elif cmd == "autoblock off" or text.lower() == 'autoblock off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = False
                                cl.sendText(msg.to,"「 Status Autoleave 」\nAutoleave telah dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                cl.sendText(msg.to,"「 Status Autoadd 」\nAutoadd telah diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                cl.sendText(msg.to,"「 Status Autoadd 」\nAutoadd telah dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["stickerOn"] = True
                                sendMention(msg.to, sender, "「 Status Sticker Check 」\n", " [ ON ]\nSilahkan kirim stickernya,\nJika sudah selesai, ketik sticker off")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["stickerOn"] = False
                                cl.sendText(msg.to,"「 Status Sticker Check 」\nSticker check dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                sendMention(msg.to, sender, "「 Status Jointicket 」\nUser ", "\nSilahkan kirim link grupnya,\nJika sudah selesai, ketik jointicket off")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                cl.sendText(msg.to,"「 Status Jointicket 」\nJointicket telah dinonaktifkan")
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  cl.sendMessage(msg.to, "「 Berhasil Diganti 」\nPesan Msg diganti jadi :\n\n{}".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  cl.sendMessage(msg.to, "「 Berhasil Diganti 」\nWelcome Msg diganti jadi :\n\n{}".format(str(spl)))

                        elif 'Set leave: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set leave: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Leave Msg")
                              else:
                                  wait["leave"] = spl
                                  cl.sendMessage(msg.to, "「 Berhasil Diganti 」\nLeave Msg diganti jadi :\n\n{}".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  cl.sendMessage(msg.to, "「 Berhasil Diganti 」\nRespon Msg diganti jadi :\n\n{}".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["RAmessage1"] = spl
                                  cl.sendMessage(msg.to, "「 Berhasil Diganti 」\nSpam Msg diganti jadi :\n\n{}".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  cl.sendMessage(msg.to, "「 Berhasil Diganti 」\nSider Msg diganti jadi :\n\n{}".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 Status Message 」\nPesan Msg mu :\n\n" + str(wait["message"]))

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 Status Welcome 」\nWelcome Msg mu :\n\n" + str(wait["welcome"]))

                        elif text.lower() == "cek leave":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 Status Leave 」\nLeave Msg mu :\n\n" + str(wait["leave"]))

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 Status Respon 」\nRespon Msg mu :\n\n" + str(wait["Respontag"]))

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 Status Spam 」\nSpam Msg mu :\n\n" + str(Setmain["RAmessage1"]))

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 Status Sider 」\nSider Msg mu :\n\n" + str(wait["mention"]))

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                   #  group1 = ki.findGroupByTicket(ticket_id)
                             

    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
