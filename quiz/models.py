from django.db import models
import datetime

class Quiz(models.Model):
    text_1      = models.CharField(max_length=400),
    text_2      = models.CharField(max_length=400),
    text_3      = models.CharField(max_length=400),
    text_4      = models.CharField(max_length=400),
    text_5      = models.CharField(max_length=400),
    text_6      = models.CharField(max_length=400),
    text_7      = models.CharField(max_length=400),
    text_8      = models.CharField(max_length=400),
    text_9      = models.CharField(max_length=400),
    text_10     = models.CharField(max_length=400),
    correct_1   = models.IntegerField(default=0),
    correct_2   = models.IntegerField(default=0),
    correct_3   = models.IntegerField(default=0),
    correct_4   = models.IntegerField(default=0),
    correct_5   = models.IntegerField(default=0),
    correct_6   = models.IntegerField(default=0),
    correct_7   = models.IntegerField(default=0),
    correct_8   = models.IntegerField(default=0),
    correct_9   = models.IntegerField(default=0),
    correct_10  = models.IntegerField(default=0),
    pub_date    = models.DateTimeField('date published', default=datetime.datetime.now())

class Invitees(models.Model):
    family_name = models.CharField(max_length=10),
    first_name  = models.CharField(max_length=10),
    email       = models.CharField(max_length=50),
    point       = models.IntegerField(default=0),
    answer_1    = models.IntegerField(default=0),
    answer_2    = models.IntegerField(default=0),
    answer_3    = models.IntegerField(default=0),
    answer_4    = models.IntegerField(default=0),
    answer_5    = models.IntegerField(default=0),
    answer_6    = models.IntegerField(default=0),
    answer_7    = models.IntegerField(default=0),
    answer_8    = models.IntegerField(default=0),
    answer_9    = models.IntegerField(default=0),
    answer_10   = models.IntegerField(default=0),
    pub_date  = models.DateTimeField('date published', default=datetime.datetime.now())