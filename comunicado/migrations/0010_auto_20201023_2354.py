# Generated by Django 3.1.1 on 2020-10-23 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunicado', '0009_auto_20201019_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='discuss',
            field=models.TextField(max_length=2200),
        ),
        migrations.AlterField(
            model_name='forum',
            name='description',
            field=models.TextField(blank=True, max_length=1200),
        ),
    ]