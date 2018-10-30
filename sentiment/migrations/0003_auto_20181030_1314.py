# Generated by Django 2.1.2 on 2018-10-30 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0002_negativetweets_positivetweets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='negativetweets',
            name='time',
            field=models.TextField(default='no time', max_length=10),
        ),
        migrations.AlterField(
            model_name='negativetweets',
            name='userName',
            field=models.TextField(default='no username', max_length=200),
        ),
        migrations.AlterField(
            model_name='positivetweets',
            name='time',
            field=models.TextField(default='no time', max_length=10),
        ),
        migrations.AlterField(
            model_name='positivetweets',
            name='userName',
            field=models.TextField(default='no username', max_length=200),
        ),
    ]
