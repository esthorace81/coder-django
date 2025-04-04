# Generated by Django 5.1.6 on 2025-03-18 00:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='producto.categoria')),
            ],
            options={
                'unique_together': {('categoria', 'nombre')},
            },
        ),
    ]
