# Generated by Django 3.1.1 on 2020-10-01 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_email',
        ),
    ]
