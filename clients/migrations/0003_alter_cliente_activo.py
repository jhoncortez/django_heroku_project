# Generated by Django 3.2.5 on 2021-07-13 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_cliente_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='activo',
            field=models.BooleanField(default=False),
        ),
    ]
