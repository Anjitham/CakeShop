# Generated by Django 5.0.2 on 2024-03-13 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_basketitem_occassion_object'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='category_name',
        ),
        migrations.RenameField(
            model_name='flavour',
            old_name='flavour',
            new_name='flavour_name',
        ),
        migrations.RenameField(
            model_name='occasion',
            old_name='occasion',
            new_name='occasion_name',
        ),
    ]