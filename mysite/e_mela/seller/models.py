# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .choices import *
# Create your models here.

class uploadItem(models.Model):
    image = models.FileField(default='')
    price = models.IntegerField()
    product_name = models.CharField(max_length=50,default='')
    discount = models.IntegerField()
    description = models.CharField(max_length=200,default='')
    product_category = models.CharField(max_length=256, choices=STATUS_CHOICES,default='')
    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.product_name
