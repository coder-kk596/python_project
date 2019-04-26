# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Doubanmoviesall(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    directors = models.CharField(max_length=1000, blank=True, null=True)
    rate = models.CharField(max_length=500, blank=True, null=True)
    cover_x = models.IntegerField(blank=True, null=True)
    star = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    casts = models.CharField(max_length=250, blank=True, null=True)
    cover = models.CharField(max_length=250, blank=True, null=True)
    id = models.CharField(max_length=100, blank=True, null=True)
    cover_y = models.IntegerField(blank=True, null=True)

class Phonejd(models.Model):
    phone_link = models.CharField(max_length=255, blank=True, null=True)
    phone_name = models.CharField(max_length=255, blank=True, null=True)
    phone_price = models.CharField(max_length=255, blank=True, null=True)
    phone_commits = models.CharField(max_length=255, blank=True, null=True)
    shop_name = models.CharField(max_length=255, blank=True, null=True)



class House(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=3000, blank=True, null=True)

class Wechatessays(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    txt_info = models.CharField(max_length=255, blank=True, null=True)
    account = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=3000, blank=True, null=True)

