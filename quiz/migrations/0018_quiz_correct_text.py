# Generated by Django 3.2.5 on 2021-10-11 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0017_quiz_explanation'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='correct_text',
            field=models.CharField(default='', max_length=100),
        ),
    ]
