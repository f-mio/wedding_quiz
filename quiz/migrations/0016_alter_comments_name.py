# Generated by Django 3.2.5 on 2021-09-26 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0015_auto_20210926_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]