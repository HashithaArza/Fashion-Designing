# Generated by Django 3.2.2 on 2021-05-11 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_fdform_clothname'),
    ]

    operations = [
        migrations.AddField(
            model_name='fdform',
            name='clothprice',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
