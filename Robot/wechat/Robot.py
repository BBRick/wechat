#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8
from multiprocessing import Process
import libevent
import threading
from RobotEvent import RobotEvent
from event_manager import event_manager
from core import Core
from multiprocessing import Pipe
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

cr = Core()
write, read = os.pipe()
recCon, sendCon = Pipe()

def wechatLogin(core):
    core.auto_login(enableCmdQR=True, hotReload=True)
    core.run()


def initLibEvent():
   return libevent.Base()

def creatEvent():
    base = initLibEvent()
    ev = libevent.Event(base, sendCon.fileno(), libevent.EV_READ|libevent.EV_PERSIST, recall, sendCon)
    ev.add(0.01)
    base.loop()

def recall(ev, fd, what, event):
    e = event.recv()
    if e:
   	print 'wechat receive', e
        sendMsgToContanct(e['msg'], account=e['account'])

@cr.msg_register('Text')
def receiveMsg(msg):
#    cr.send(msg="不要调戏调戏机器人哦~n(*≧▽≦*)n", toUserName=msg['FromUserName'])

    pass

@cr.msg_register('Text', isGroupChat=True)
def receiveGrope(msg):
    sendCon.send(msg)
    pass

#@cr.msg_register('Friends')
#def receiveAddFriend(msg):
#    msg.user.verify()
#    msg.user.send('欢迎添加机器人 王者小机 !')

def sendMsgToGroup(msg, groupName):
    group = cr.search_chatrooms(name=groupName)
    if group:
	cr.send(msg, toUserName=group[0]['UserName'])


def sendMsgToContanct(msg, account):
    contact = cr.search_friends(name=account)
    print cr.memberList
    print contact
    if contact:
	cr.send(msg, toUserName=contact[0]['UserName'])


if __name__ == '__main__':
    manager = event_manager(robotCon=recCon)
    manager.setConfig()
    t = threading.Thread(target=creatEvent)
    t.start()
    wechatLogin(cr)



