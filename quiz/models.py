from django.db import models
from django.utils import timezone
import datetime

class Quiz(models.Model):
    quiz_title    = models.CharField(max_length=10, default="")
    quiz_category = models.CharField(max_length=10, default="")
    quiz_text     = models.CharField(max_length=400, default="")
    quiz_correct  = models.IntegerField(default=0)
    choices_1     = models.CharField(max_length=100, default="")
    choices_2     = models.CharField(max_length=100, default="")
    choices_3     = models.CharField(max_length=100, default="")
    choices_4     = models.CharField(max_length=100, default="")
    pub_date      = models.DateTimeField('date published')

    def __str__(self):
        return self.quiz_title + " 【" + self.quiz_category +"】"

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

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

    def __str__(self):
        return ("{} {} pont : {}".format(self.family_name, self.first_name, self.point))

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
