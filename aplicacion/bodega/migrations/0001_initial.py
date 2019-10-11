# Generated by Django 2.2.5 on 2019-10-11 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompraInsumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True, verbose_name='registro activo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('ip_creacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de creación')),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True, verbose_name='fecha de modificación')),
                ('ip_modificacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de modificación')),
                ('unidades', models.IntegerField(verbose_name='unidades')),
                ('precio_unitario', models.IntegerField(verbose_name='precio unitario')),
                ('valor_compra', models.IntegerField(blank=True, null=True, verbose_name='valor de la compra')),
            ],
            options={
                'verbose_name': 'compra de insumo',
                'verbose_name_plural': 'compras de insumos',
            },
        ),
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True, verbose_name='registro activo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('ip_creacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de creación')),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True, verbose_name='fecha de modificación')),
                ('ip_modificacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de modificación')),
                ('nombre', models.CharField(max_length=30, verbose_name='nombre')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='descripción')),
            ],
            options={
                'verbose_name': 'insumo',
                'verbose_name_plural': 'insumos',
            },
        ),
        migrations.CreateModel(
            name='InsumoDetallado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True, verbose_name='registro activo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('ip_creacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de creación')),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True, verbose_name='fecha de modificación')),
                ('ip_modificacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de modificación')),
                ('cantidad', models.IntegerField(verbose_name='cantidad')),
            ],
            options={
                'verbose_name': 'insumo detallado',
                'verbose_name_plural': 'insumos detallados',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True, verbose_name='registro activo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('ip_creacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de creación')),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True, verbose_name='fecha de modificación')),
                ('ip_modificacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de modificación')),
                ('nombre', models.CharField(max_length=10, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'marca',
                'verbose_name_plural': 'marcas',
            },
        ),
        migrations.CreateModel(
            name='ProduccionProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True, verbose_name='registro activo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('ip_creacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de creación')),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True, verbose_name='fecha de modificación')),
                ('ip_modificacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de modificación')),
                ('lote', models.IntegerField(default=0, verbose_name='lote')),
                ('unidades_producidas', models.IntegerField(blank=True, null=True, verbose_name='unidades producidas')),
                ('precio_costo', models.IntegerField(blank=True, null=True, verbose_name='precio de costo')),
                ('fecha_elaboracion', models.DateField(verbose_name='fecha de elaboración')),
                ('fecha_vencimiento', models.DateField(verbose_name='fecha de vencimiento')),
            ],
            options={
                'verbose_name': 'producción de producto',
                'verbose_name_plural': 'producción de productos',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True, verbose_name='registro activo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('ip_creacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de creación')),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True, verbose_name='fecha de modificación')),
                ('ip_modificacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de modificación')),
                ('nombre', models.CharField(max_length=30, verbose_name='nombre')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='descripción')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
            },
        ),
        migrations.CreateModel(
            name='ProductoDetallado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True, verbose_name='registro activo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('ip_creacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de creación')),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True, verbose_name='fecha de modificación')),
                ('ip_modificacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de modificación')),
                ('cantidad', models.IntegerField(verbose_name='cantidad')),
                ('precio_venta', models.IntegerField(verbose_name='precio de venta')),
                ('unidades_disponibles', models.IntegerField(blank=True, default=0, null=True, verbose_name='unidades disponibles')),
            ],
            options={
                'verbose_name': 'producto detallado',
                'verbose_name_plural': 'productos detallados',
            },
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True, verbose_name='registro activo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('ip_creacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de creación')),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True, verbose_name='fecha de modificación')),
                ('ip_modificacion', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de modificación')),
                ('nombre', models.CharField(max_length=10, verbose_name='nombre')),
                ('abreviatura', models.CharField(max_length=3, verbose_name='abreviatura')),
            ],
            options={
                'verbose_name': 'unidad de medida',
                'verbose_name_plural': 'unidades de medida',
            },
        ),
    ]
