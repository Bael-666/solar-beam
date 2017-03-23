# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 06:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tarifas', '0004_tarifa1x_dac'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreasControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AreasControl', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=200)),
                ('AreaCont', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarifas.AreasControl')),
            ],
        ),
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estados', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='ciudades',
            name='Estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarifas.Estados'),
        ),
    ]