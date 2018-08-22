# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class BookType(models.Model):
    TypeNum = models.IntegerField(primary_key=True)
    TypeName = models.CharField(max_length=20)
    def __unicode__(self):
        return '%s' % (self.TypeName)
    objects = StudentManager()

class StudentManager(models.Manager):

    def create_book(self, typeName):
        book = self.create(TypeName=typeName)
        return book

