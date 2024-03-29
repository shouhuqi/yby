#!/usr/bin/env python
# coding=utf-8
#--------------#--------------#
# @Author: YJR-1100
# @Date: 2022-03-22 16:23:55
# @LastEditors: YJR-1100
# @LastEditTime: 2022-04-21 16:27:14
# @FilePath: \wx_RoomOrder\RoomOrderbackend\apps\orderitem\api.py
# @Description:
# @
# @Copyright (c) 2022 by yjr-1100/CSU, All Rights Reserved.
#--------------#--------------#

from operator import and_
from flask import Blueprint, request
from apps.orderitem.models import Orderitems
from apps.rooms.models import Rooms
from apps.users.models import Users
from apps.managers.models import Managers
from apps.organizations.models import Organizations
from common.sqlalchemy2json import AlchemyEncoder
from exts import db
from sqlalchemy import or_
from datetime import date, datetime
from common.result import trueReturn, falseReturn
import time
orderitems_bp = Blueprint('orderitems', __name__)

# 预约的接口


@orderitems_bp.route('/makeorder', methods=['POST'])
def makeorder():
    # 今天的日期
    print(date.today())
    data = request.get_json()
    print("xxxxx makeorder:", data)
    myorder = Orderitems()
    try:
        myorder.odatetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        myorder.user_id = data['user_id']
        myorder.room_id = data['room_id']
        myorder.room2orgid = data['room2orgid']
        myorder.usingtime = data["usingdate"]+" "+data["usingtime"]
        myorder.roomusage = data["roomusage"]

        myorder.autograph = "1;0"

        ##TODO
        myorder.ostatus = 1
    except Exception as e:
        return falseReturn(msg=e, code=-1)
    try:
        db.session.add(myorder)
        db.session.commit()
        return trueReturn(msg="预约提交成功")
    except:
        return falseReturn(msg="数据库错误", code=-2)

# 审核接口


@orderitems_bp.route('/checkorder', methods=['POST'])
def checkorder():
    data = request.get_json()
    print(data)
    try:
        oid = data['oid']
        status = data['status']
        checker_id = data['checker_id']
    except:
        return falseReturn(msg="no oid")
    myorder = Orderitems.query.filter(Orderitems.oid == oid).first()
    if status == 0:
        myorder.rejectreasion = data['value']
    try:
        myorder.ostatus = status
        myorder.ochecktime = datetime.now().strftime('%Y-%m-%d %H:%M')
        myorder.checker_id = checker_id
        db.session.commit()
    except Exception as e:
        print(e)
        return falseReturn(msg="数据库错误")
    return trueReturn(msg="操作成功")

# 所有管理的教室的所有预约的状态


@orderitems_bp.route('/managergetorder', methods=['POST'])
def managergetorder():
    data = request.get_json()
    try:
        orgid = data['orgid']
    except:
        return falseReturn(msg="缺少必要参数")
    orderitems = Orderitems.query.filter(Orderitems.room2orgid == orgid).all()
    orderlist = []
    for item in orderitems:
        order = {}
        order['oid'] = item.oid
        order['username'] = Users.query.get(item.user_id).uname
        order['uphonenum'] = Users.query.get(item.user_id).uphonenum
        order['schoolid'] = 0
        order['ordertime'] = str(item.odatetime)
        order['roomname'] = Rooms.query.get(item.room_id).rname
        order['address'] = Rooms.query.get(item.room_id).raddress
        order['roomusage'] = item.roomusage
        order['usingtime'] = item.usingtime
        order['status'] = item.ostatus
        if(item.ochecktime):
            order['ochecktime'] = str(item.ochecktime)
        if(item.checker_id):
            order['checkername'] = Managers.query.get(item.checker_id).mname
        if(item.rejectreasion):
            order['rejectreasion'] = item.rejectreasion
            order['userinner'] = 1
            order['autograph'] = item.autograph
        orderlist.append(order)
    # print(orderlist)
    return trueReturn(data=orderlist)


@orderitems_bp.route('/getmyorders', methods=['POST'])
def getmyorders():
    data = request.get_json()
    try:
        uid = data['uid']
    except:
        return falseReturn(msg="缺少必要参数", code=1)
    orderitems = Orderitems.query.filter(Orderitems.user_id == uid).all()
    orderlist = []
    for item in orderitems:
        order = {}
        order['oid'] = item.oid
        order['uphonenum'] = Users.query.get(item.user_id).uphonenum
        order['schoolid'] = 0
        order['username'] = Users.query.get(item.user_id).uname
        order['ordertime'] = str(item.odatetime)
        order['roomname'] = Rooms.query.get(item.room_id).rname
        order['address'] = Rooms.query.get(item.room_id).raddress
        order['roomusage'] = item.roomusage
        order['usingtime'] = item.usingtime
        order['status'] = item.ostatus
        if(item.ochecktime):
            order['ochecktime'] = str(item.ochecktime)
        if(item.checker_id):
            order['checkername'] = Managers.query.get(item.checker_id).mname
        if(item.rejectreasion):
            order['rejectreasion'] = item.rejectreasion
            order['userinner'] = 1
            order['autograph'] = item.autograph
        orderlist.append(order)
    return trueReturn(data=orderlist)

# 得到该教室今天可用时间


@orderitems_bp.route('/roomusertoday', methods=['GET'])
def roomusertoday():
    try:
        rid = request.args.get('rid')
        date = request.args.get('date')
    except:
        return falseReturn(msg="参数错误", code=-1)
    # roomusedtime = Orderitems.query.order_by(Orderitems.usingtime.desc()).filter(and_(Orderitems.room_id==rid,Orderitems.usingtime.contains(date)),Orderitems.ostatus==1).all()
    roomusedtime = Orderitems.query.filter(and_(
        Orderitems.room_id == rid, Orderitems.usingtime.contains(date)), Orderitems.ostatus == 1).all()
    usedtimelist = []
    for room in roomusedtime:
        usedtimelist.append(room.usingtime.split(' ')[1])
    return trueReturn(data=usedtimelist)
