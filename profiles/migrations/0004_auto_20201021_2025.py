# Generated by Django 3.1.1 on 2020-10-21 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20201014_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_team',
            field=models.IntegerField(),
        ),
    ]
