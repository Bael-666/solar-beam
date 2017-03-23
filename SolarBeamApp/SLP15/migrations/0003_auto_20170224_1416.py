# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 20:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SLP15', '0002_auto_20170224_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='central',
            name='central',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='centrales',
            name='central',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SLP15.Central'),
        ),
        migrations.AlterField(
            model_name='centrales',
            name='gen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SLP15.Gen'),
        ),
        migrations.AlterField(
            model_name='centralov',
            name='central',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SLP15.Central'),
        ),
        migrations.AlterField(
            model_name='centralov',
            name='gen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SLP15.Gen'),
        ),
        migrations.AlterField(
            model_name='centralov',
            name='paquetes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SLP15.Paquetes'),
        ),
        migrations.AlterField(
            model_name='ofererc',
            name='erc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SLP15.Erc'),
        ),
        migrations.AlterField(
            model_name='ofererc',
            name='ofertas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SLP15.Ofertas'),
        ),
        migrations.AlterField(
            model_name='paqexc',
            name='conpaqexc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SLP15.Conpaqexc'),
        ),
        migrations.AlterField(
            model_name='paqexc',
            name='gen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SLP15.Gen'),
        ),
        migrations.AlterField(
            model_name='paqexc',
            name='paquetes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SLP15.Paquetes'),
        ),
        migrations.AlterField(
            model_name='paqgen',
            name='gen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SLP15.Gen'),
        ),
        migrations.AlterField(
            model_name='paqgen',
            name='paquetes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SLP15.Paquetes'),
        ),
        migrations.AlterField(
            model_name='paqin',
            name='gen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SLP15.Gen'),
        ),
        migrations.AlterField(
            model_name='paqin',
            name='paquetes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SLP15.Paquetes'),
        ),
        migrations.AlterField(
            model_name='paqin',
            name='paquetes2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SLP15.Paquetes2'),
        ),
    ]