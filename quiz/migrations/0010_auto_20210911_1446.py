# Generated by Django 3.2.5 on 2021-09-11 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_auto_20210911_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitees',
            name='answer_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='invitees',
            name='answer_10',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='invitees',
            name='answer_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='invitees',
            name='answer_3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='invitees',
            name='answer_4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='invitees',
            name='answer_5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='invitees',
            name='answer_6',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='invitees',
            name='answer_7',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='invitees',
            name='answer_8',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='invitees',
            name='answer_9',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='invitees',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='invitees',
            name='family_name',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='invitees',
            name='first_name',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='invitees',
            name='point',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='quiz',
            name='quiz_correct',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='quiz',
            name='quiz_text',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='invitees',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
