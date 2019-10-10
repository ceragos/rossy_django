# Generated by Django 2.2.5 on 2019-10-09 21:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientes', '0002_auto_20191009_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='creado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cliente_creado_por', to=settings.AUTH_USER_MODEL, verbose_name='creado por'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cliente_modificado_por', to=settings.AUTH_USER_MODEL, verbose_name='modificado por'),
        ),
    ]
