# Generated by Django 3.2.5 on 2021-09-09 23:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20210910_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitees',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 10, 8, 1, 23, 5320), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 10, 8, 1, 22, 946378), verbose_name='date published'),
        ),
    ]
