# Generated by Django 3.2.5 on 2021-09-12 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0012_quiz_quiz_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='quiz_category',
            field=models.CharField(default='', max_length=10),
        ),
    ]
