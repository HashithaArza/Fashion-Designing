# Generated by Django 3.2.2 on 2021-05-11 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_fdform_clothprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='fdform',
            name='email',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='fdform',
            name='username',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
