from django.db import models


class Quiz(models.Model):
    quiz_title    = models.CharField(max_length=10, default="")
    quiz_category = models.CharField(max_length=10, default="")
    quiz_text     = models.TextField(max_length=400, default="")
    quiz_correct  = models.IntegerField(default=0)
    correct_text  = models.CharField(max_length=100, default="")
    explanation   = models.TextField(max_length=600, default="")
    choice_1      = models.CharField(max_length=100, default="")
    choice_2      = models.CharField(max_length=100, default="")
    choice_3      = models.CharField(max_length=100, default="")
    choice_4      = models.CharField(max_length=100, default="")
    pub_date      = models.DateTimeField('date published')

    def __str__(self):
        return self.quiz_title + " 【" + self.quiz_category +"】"


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
        return ("{} {} point : {}".format(self.family_name, self.first_name, self.point))


class Comments(models.Model):
    name    = models.CharField(max_length=50, blank=True, null=True)
    comment = models.TextField(max_length=800)
    pub_date    = models.DateTimeField('date published')

    def __str__(self):
        return self.comment