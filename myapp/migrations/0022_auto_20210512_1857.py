# Generated by Django 3.2.2 on 2021-05-12 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_alter_cuitems_clothgender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuitems',
            name='clothcolour',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cuitems',
            name='clothname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cuitems',
            name='clothpattern',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cuitems',
            name='clothprice',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cuitems',
            name='clothsizes',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cuitems',
            name='clothtype',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cuitems',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
