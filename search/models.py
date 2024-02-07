# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Documents(models.Model):
    title = models.CharField(max_length=150, verbose_name=("Title"))
    content = models.TextField(max_length=250, verbose_name=("content"))

    def __str__(self):
        return self.title


