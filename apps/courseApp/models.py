# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Description(models.Model):
    course_name = models.OneToOneField(
        Courses,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    desc = models.CharField(max_length=255)

    def __str__(self):
        return self.desc
