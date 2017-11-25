# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 04:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_type', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('category_name', models.CharField(default='', max_length=250)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Laptops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=1000)),
                ('price', models.IntegerField(default=0)),
                ('discounted_price', models.IntegerField(default=0)),
                ('product_content', models.CharField(default='', max_length=1000)),
                ('color', models.CharField(default='', max_length=250)),
                ('graphics_ram', models.CharField(default='', max_length=20)),
                ('brand', models.CharField(default='', max_length=100)),
                ('processor', models.CharField(default='', max_length=100)),
                ('ssd', models.CharField(default='', max_length=100)),
                ('ram', models.CharField(default='', max_length=100)),
                ('ram_type', models.CharField(default='', max_length=100)),
                ('storage', models.CharField(default='', max_length=250)),
                ('display', models.CharField(default='', max_length=250)),
                ('warranty_summary', models.CharField(default='', max_length=2000)),
                ('image_src', models.CharField(default='', max_length=2000)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kompany.Category')),
            ],
            options={
                'verbose_name': 'Laptop',
                'verbose_name_plural': 'Laptops',
            },
        ),
        migrations.CreateModel(
            name='Mobiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=1000)),
                ('price', models.IntegerField(default=0)),
                ('discounted_price', models.IntegerField(default=0)),
                ('model_name', models.CharField(default='', max_length=1000)),
                ('color', models.CharField(default='', max_length=250)),
                ('display_size', models.CharField(default='', max_length=100)),
                ('resolution', models.CharField(default='', max_length=100)),
                ('ram', models.CharField(default='', max_length=100)),
                ('storage', models.CharField(default='', max_length=100)),
                ('primary_camera', models.CharField(default='', max_length=250)),
                ('secondary_camera', models.CharField(default='', max_length=250)),
                ('warranty_summary', models.CharField(default='', max_length=2000)),
                ('image_src', models.CharField(default='', max_length=2000)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kompany.Category')),
            ],
            options={
                'verbose_name': 'Mobile',
                'verbose_name_plural': 'Mobiles',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(default='', max_length=1000)),
                ('stock', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('discounted_price', models.IntegerField(default=0)),
                ('image_count', models.IntegerField(default=0)),
                ('category_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kompany.Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.AddField(
            model_name='mobiles',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kompany.Products'),
        ),
        migrations.AddField(
            model_name='laptops',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kompany.Products'),
        ),
    ]
