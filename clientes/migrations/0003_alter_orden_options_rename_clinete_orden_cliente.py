# Generated by Django 5.1.4 on 2024-12-19 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_servicio_orden_ordenservicio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orden',
            options={'verbose_name': 'Orden', 'verbose_name_plural': 'Órdenes'},
        ),
        migrations.RenameField(
            model_name='orden',
            old_name='clinete',
            new_name='cliente',
        ),
    ]
