# Generated by Django 2.2.5 on 2019-09-22 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20190922_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='eliminado',
        ),
    ]
