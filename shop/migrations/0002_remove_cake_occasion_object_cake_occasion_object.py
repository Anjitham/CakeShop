# Generated by Django 5.0.2 on 2024-02-29 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cake',
            name='Occasion_object',
        ),
        migrations.AddField(
            model_name='cake',
            name='Occasion_object',
            field=models.ManyToManyField(to='shop.occasion'),
        ),
    ]
