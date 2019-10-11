# Generated by Django 2.2.5 on 2019-10-11 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbonoCredito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True, verbose_name='registro activo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('ip_creacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de creación')),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True, verbose_name='fecha de modificación')),
                ('ip_modificacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de modificación')),
                ('fecha_abono', models.DateTimeField(verbose_name='fecha del abono')),
                ('valor_abono', models.IntegerField(blank=True, null=True, verbose_name='valor del abono')),
            ],
            options={
                'verbose_name': 'Abono del crédito',
                'verbose_name_plural': 'Abonos del crédito',
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True, verbose_name='registro activo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('ip_creacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de creación')),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True, verbose_name='fecha de modificación')),
                ('ip_modificacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de modificación')),
                ('fecha_compra', models.DateTimeField(verbose_name='fecha de compra')),
                ('contado', models.BooleanField(default=False, verbose_name='contado')),
                ('credito', models.BooleanField(default=False, verbose_name='credito')),
                ('pagada', models.BooleanField(default=False, verbose_name='pagada')),
                ('fecha_pago', models.DateField(blank=True, help_text='Uselo solo si selecciono crédito como método de pago.', null=True, verbose_name='fecha de pago')),
                ('total', models.IntegerField(blank=True, default=0, null=True, verbose_name='total de la factura')),
            ],
            options={
                'verbose_name': 'factura',
                'verbose_name_plural': 'facturas',
            },
        ),
        migrations.CreateModel(
            name='ProductoVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True, verbose_name='registro activo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('ip_creacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de creación')),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True, verbose_name='fecha de modificación')),
                ('ip_modificacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de modificación')),
                ('unidades_vendidas', models.IntegerField(verbose_name='unidades vendidas')),
                ('precio_venta', models.IntegerField(blank=True, default=0, null=True, verbose_name='precio de venta')),
                ('valor_venta', models.IntegerField(blank=True, default=0, null=True, verbose_name='valor de la venta')),
            ],
            options={
                'verbose_name': 'producto vendido',
                'verbose_name_plural': 'productos vendidos',
            },
        ),
    ]
