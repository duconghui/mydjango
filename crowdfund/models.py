# coding=utf-8
from django.db import models


# Create your models here.
# 关联
# 1.投资人（1）和项目（n）
# 2.投资人（1）和业务（n）
# 3.发起人（1）和项目（n）
# 4.发起人（1）和业务（n）
# 5.项目（1）和业务（n）


class User(models.Model):  # 用户表（只用于注册登陆）
    user_id = models.AutoField(primary_key=True)  # 用户id
    userName = models.CharField(max_length=20)  # 用户名
    userPwd = models.CharField(max_length=20)  # 用户密码
    real_name = models.CharField(max_length=20)  # 用户真实姓名
    email = models.CharField(max_length=20)  # 用户邮箱
    phone = models.CharField(max_length=11)  # 联系方式
    avatar = models.CharField(max_length=128)  # 用户头像


class Investor(models.Model):  # 投资人表
    investor_id = models.AutoField(primary_key=True)  # 投资人id
    user_id = models.CharField(max_length=20)  # 用户id
    disposable_funds = models.CharField(max_length=20)  # 投资人可支配资金
    expenditure = models.CharField(max_length=20,default='0')  # 投资人支出
    recharge = models.CharField(max_length=20,default='0')  # 投资人充值
    SELVALUE_state = (
        ('one', '认证成功'),  # 前面是展示在前端界面的内容,后面的'one'是真正存在数据库中的
        ('two', '未认证'),
    )
    state = models.CharField(max_length=10, choices=SELVALUE_state)  # 投资人申请状态
    item_id = models.CharField(max_length=10)  # 投资项目id


class Originator(models.Model):  # 项目发起人表
    originator_id = models.AutoField(primary_key=True)  # 项目发起人id
    user_id = models.CharField(max_length=20)  # 用户id
    item_id = models.CharField(max_length=10)  # 项目id


class Item(models.Model):  # 项目表
    item_id = models.AutoField(primary_key=True)  # 项目id
    title = models.CharField(max_length=60)  # 项目名称
    short_title = models.CharField(max_length=30)  # 项目简称
    SELVALUE_ind_id = (
        ('one', '移动互联'),  # 前面是展示在前端界面的内容,后面的'one'是真正存在数据库中的
        ('two', '节能环保'),
        ('three', '文化传媒'),
        ('four', '新能源'),
        ('five', '消费服务'),
        ('six', '其他'),
    )
    ind_id = models.CharField(max_length=10, choices=SELVALUE_ind_id)  # 项目行业
    SELVALUE_country = (
        ('one', '北京'),  # 前面是展示在前端界面的内容,后面的'one'是真正存在数据库中的
        ('two', '天津'),
        ('three', '浙江'),
        ('four', '上海'),
        ('five', '福建'),
        ('six', '湖北'),
        ('seven', '其他'),
    )
    country = models.CharField(max_length=10, choices=SELVALUE_country)  # 项目地区
    SELVALUE_phase = (
        ('one', '种子期'),  # 前面是展示在前端界面的内容,后面的'first'是真正存在数据库中的
        ('two', '成长期'),
        ('three', '扩张期'),
        ('four', '成熟期'),
    )
    phase = models.CharField(max_length=10, choices=SELVALUE_phase)  # 项目阶段
    amount = models.CharField(max_length=40)  # 项目计划融资金额
    transfer_ratio = models.CharField(max_length=40)  # 项目计划让出股份
    summary = models.CharField(max_length=40)  # 项目介绍
    link_url = models.CharField(max_length=11)  # 项目网址
    originator_id = models.CharField(max_length=20)  # 项目发起人id
    raised_funds = models.CharField(max_length=20)  # 已筹资金


class Business(models.Model):  # 业务表
    id = models.AutoField(primary_key=True)  # 主键
    inflow_funds = models.CharField(max_length=20)  # 资金流入
    outflow_funds = models.CharField(max_length=20)  # 资金流出
    support_num = models.CharField(max_length=20)  # 支持人数
    raised_funds = models.CharField(max_length=20)  # 已筹资金
    remaining_data = models.CharField(max_length=10)  # 剩余日期
