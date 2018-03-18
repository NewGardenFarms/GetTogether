# Generated by Django 2.0 on 2018-03-04 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20180227_0358'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='categories',
            field=models.ManyToManyField(blank=True, to='events.Category'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='topics',
            field=models.ManyToManyField(blank=True, to='events.Topic'),
        ),
    ]