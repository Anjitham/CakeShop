# Generated by Django 5.0.2 on 2024-03-13 16:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_rename_occasion_occasion_occasion'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketitem',
            name='occassion_object',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.occasion'),
        ),
    ]
