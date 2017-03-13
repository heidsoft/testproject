# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=127)

    def __unicode__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=127)
    author = models.ForeignKey(Author)

    '''
    实现unicode()内嵌函数；应该返回Unicode对象。当没有定义这个方法时，取而代之的是string转换，转换的结果是用系统默认编码转化为Unicode。
    '''
    def __unicode__(self):
        return self.name