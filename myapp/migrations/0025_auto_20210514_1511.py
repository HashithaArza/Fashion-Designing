# Generated by Django 3.2.2 on 2021-05-14 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_cuitems_clothdesigner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuitems',
            name='clothprice',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='fdform',
            name='clothprice',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True),
        ),
    ]
