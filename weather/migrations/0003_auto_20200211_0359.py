# Generated by Django 3.0.3 on 2020-02-11 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_signup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='signup',
            name='location',
            field=models.CharField(default='SOME STRING', max_length=256),
        ),
    ]
