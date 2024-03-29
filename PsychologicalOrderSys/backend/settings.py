#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-22 14:26:49
# @LastEditors: YJR-1100
# @LastEditTime: 2022-04-24 17:15:13
# @FilePath: \wx_RoomOrder\RoomOrderbackend\settings.py
# @Description:
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
#--------------#--------------#
import json
# 为app创建的配置文件
import os


class Config:
    ENV = 'development'
    DEBUG = True
    # 使用的数据库+驱动://user:password@hostip:port/databasename
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1:3306/roomorder?charset=utf8'
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_ECHO = True
    WXAPPSETTINGPATH = "./wxappsetting.json"


class DevelopmentConfig(Config):
    ENV = 'development'


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False

# 小程序的id 和 密钥


class wxappConfig(Config):
    appsetting = json.load(open(Config.WXAPPSETTINGPATH))
    appid = appsetting['appid']
    appsecret = appsetting['appsecret']


class defaultimage():
    room_UPLOAD_img = os.path.abspath(
        os.path.dirname(__file__))+'/uploadstatic/photo/'
    room_UPLOAD_pdf = os.path.abspath(
        os.path.dirname(__file__))+'/uploadstatic/pdf/'
    showroomimgurl = 'http://119.45.10.111:80/backend/api/v1/room/show/'
    dowloadroompdf = 'http://119.45.10.111:80/backend/api/v1/room/getroompdf/'
    swiper_UPLOAD_img = os.path.abspath(
        os.path.dirname(__file__))+'/uploadstatic/swiper/'
    showswiperimgurl = 'http://119.45.10.111:80/backend/api/v1/swiper/show/'
    swiperdefaultimage = "https://cdn.jsdelivr.net/gh/yjr-1100/Photobag/roomorderimage/202203261650698.jpg"
    access_UPLOAD_img = os.path.abspath(
        os.path.dirname(__file__))+'/uploadstatic/accessimg/'
    showsaccessimgurl = 'http://119.45.10.111:80/backend/api/v1/user/show/'
