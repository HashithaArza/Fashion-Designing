# Generated by Django 3.2.2 on 2021-05-16 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_auto_20210514_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuitems',
            name='cart',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='cuitems',
            name='wishlist',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
