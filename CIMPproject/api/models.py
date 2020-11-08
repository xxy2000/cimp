from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# 可以通过 命令 python  manage.py createsuperuser 来创建超级管理员


class User(AbstractUser):
    # 创建user表，包含管理员，学生，老师，一共三个属性
    id = models.BigAutoField(primary_key=True)
    # 用户类型
    # 1： 超管 | 1000： 普通管理员  | 2000：学生  |  3000： 老师
    usertype = models.PositiveIntegerField()
    # 真实姓名
    realname = models.CharField(max_length=30, db_index=True)
    # 学号
    studentno = models.CharField(
        max_length=10,
        db_index=True,
        null=True, blank=True
    )
    # 备注描述
    desc = models.CharField(max_length=500, null=True, blank=True)

    REQUIRED_FIELDS = ['usertype', 'realname']

    class Meta:
        db_table = "by_user"


class Notification(models.Model):
    # 创建通知表，里面包含所有的通知内容，只能由管理员创建通知
    # 通知创建时间
    pubdate = models.DateTimeField(default=datetime.datetime.now)
    # 公告名字
    title = models.CharField(max_length=100)
    # 创建者
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    # 内容
    content = models.CharField(max_length=2000)
    # 状态
    status = models.PositiveIntegerField(default=1)


class News(models.Model):
    # 创建新闻表，里面包含所有的新闻内容，只能由管理员创建新闻
    # 通知创建时间
    pubdate = models.DateTimeField(default=datetime.datetime.now)
    # 公告名字
    title = models.CharField(max_length=100)
    # 创建者
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    # 内容
    content = models.CharField(max_length=2000)
    # 状态
    status = models.PositiveIntegerField(default=1)


class Paper(models.Model):
    # 创建论文表， 里面包含所有的论文内容， 所有User都可以创建论文
    # 通知创建时间
    pubdate = models.DateTimeField(default=datetime.datetime.now)
    # 公告名字
    title = models.CharField(max_length=100)
    # 创建者
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    # 内容
    content = models.CharField(max_length=2000)
    # 点赞数
    thumbupcount = models.PositiveIntegerField(default=0)
    # 状态
    status = models.PositiveIntegerField(default=1)


class Like(models.Model):
    # 创建Like表，用于统计论文点赞
    # 点赞的user.id
    uid = models.PositiveIntegerField()
    # 点赞的paper.id
    pid = models.PositiveIntegerField()


class Students(models.Model):
    # 创建Students表用于关联学生和老师
    # 创建者ID
    sid = models.PositiveIntegerField(unique=True)
    # 老师
    Tea = models.ForeignKey(User, on_delete=models.PROTECT)


class Workflow(models.Model):
    # 创建工作流表，包含毕业工作流的工作步骤
    # 创建者
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    # 标题
    title = models.CharField(max_length=100)
    # 状态
    currentstate = models.CharField(max_length=20)
    # 创建日期
    createdate = models.DateTimeField(default=datetime.datetime.now)


class Workstep(models.Model):
    # 创建工作流步骤表，包含毕业工作流的具体步骤内容
    # 所属的工作流
    workflow = models.ForeignKey(Workflow, on_delete=models.PROTECT)
    # 工作流创建者名
    operator = models.ForeignKey(User, on_delete=models.PROTECT)
    # 创建时间
    actiondate = models.DateTimeField(default=datetime.datetime.now)
    # 工作流步骤名
    actionname = models.CharField(max_length=200)
    # 下一个工作步骤
    nextstate = models.CharField(max_length=200)
    # 数据备注
    name = models.CharField(max_length=20, default='备注')
    # 数据类型
    type = models.CharField(max_length=20)
    # 数据内容
    value = models.CharField(max_length=2000)
