# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# 调用内置用户管理
class VmaigUser(AbstractUser):
    img = models.CharField(max_length=200, default='/static/tx/default.jpg',
                           verbose_name=u'头像地址')
    intro = models.CharField(max_length=200, blank=True, null=True,
                             verbose_name=u'个性签名')


