# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 20:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tarifas', '0019_auto_20170320_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='DAC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fijo', models.FloatField(default=0)),
                ('Costo_kWh', models.FloatField(default=0)),
                ('Anio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tarifas.Anio')),
                ('AreaCont', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarifas.AreasControl')),
                ('Mes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tarifas.Meses')),
                ('Temp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tarifas.Temporada')),
            ],
        ),
    ]