# Generated by Django 3.2.5 on 2021-09-09 23:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitees',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 10, 8, 0, 19, 258824), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 10, 8, 0, 19, 228264), verbose_name='date published'),
        ),
    ]
