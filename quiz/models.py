from django.db import models

class Quiz(models.Model):
    quiz_text     = models.CharField(max_length=400, default="")
    quiz_correct  = models.IntegerField(default=0)
    pub_date      = models.DateTimeField('date published')

class Invitees(models.Model):
    family_name = models.CharField(max_length=10, default="")
    first_name  = models.CharField(max_length=10, default="")
    email       = models.CharField(max_length=50, blank=True, null=True)
    point       = models.IntegerField(default=0)
    answer_1    = models.IntegerField(default=0)
    answer_2    = models.IntegerField(default=0)
    answer_3    = models.IntegerField(default=0)
    answer_4    = models.IntegerField(default=0)
    answer_5    = models.IntegerField(default=0)
    answer_6    = models.IntegerField(default=0)
    answer_7    = models.IntegerField(default=0)
    answer_8    = models.IntegerField(default=0)
    answer_9    = models.IntegerField(default=0)
    answer_10   = models.IntegerField(default=0)
    pub_date    = models.DateTimeField('date published')