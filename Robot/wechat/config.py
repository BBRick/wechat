#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8
import os, platform

VERSION = '1.3.8'
BASE_URL = 'https://login.weixin.qq.com'
OS = platform.system() # Windows, Linux, Darwin
DIR = os.getcwd()
DEFAULT_QR = 'QR.png'
TIMEOUT = (10, 60)

USER_AGENT = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
KAFKA_HOST = 'kafka.t.smartdata-x.com'
KAFKA_RECEIVE_TOPIC = 'specialplane_hz_push_robot'
KAFKA_SEND_TOPIC = 'specialplane_hz_push_service'
SQL_HOST = '139.224.18.190'
SQL_USER = 'smobaspecialplane'
SQL_PASSWD = 'smobaspecialplane!@#$%^'
SQL_DBNAME = 'smoba_special_plane_t'
SQL_PORT = 3306
SQL_CHARSET = 'utf8'

WIN_RATE_IDENTIFIER = '此次航班胜负:'

EVALUTE_IDENTIFIER = '本次航班已经着陆'
