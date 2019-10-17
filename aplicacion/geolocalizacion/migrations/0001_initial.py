# Generated by Django 2.2.5 on 2019-10-17 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True, verbose_name='registro activo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('ip_creacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de creación')),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True, verbose_name='fecha de modificación')),
                ('ip_modificacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de modificación')),
                ('nombre', models.CharField(blank=True, max_length=30, null=True, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'barrio',
                'verbose_name_plural': 'barrios',
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True, verbose_name='registro activo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('ip_creacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de creación')),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True, verbose_name='fecha de modificación')),
                ('ip_modificacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de modificación')),
                ('nombre', models.CharField(blank=True, max_length=30, null=True, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'ciudad',
                'verbose_name_plural': 'ciudades',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True, verbose_name='registro activo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('ip_creacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de creación')),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True, verbose_name='fecha de modificación')),
                ('ip_modificacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de modificación')),
                ('nombre', models.CharField(blank=True, max_length=30, null=True, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'departamento',
                'verbose_name_plural': 'departamentos',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True, verbose_name='registro activo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('ip_creacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de creación')),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True, verbose_name='fecha de modificación')),
                ('ip_modificacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de modificación')),
                ('nombre', models.CharField(blank=True, max_length=30, null=True, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'país',
                'verbose_name_plural': 'países',
            },
        ),
    ]
