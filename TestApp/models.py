from django.db import models
from datetime import datetime

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'姓名')
    mobile = models.CharField(max_length=11, verbose_name=u'手机号码')


class Book(models.Model):
    author = models.ForeignKey(Author, related_name="FAN")
    bookname = models.CharField(max_length=30, verbose_name=u'书名')
    pubtime = models.DateField(default=datetime.now(), verbose_name='出版时间')