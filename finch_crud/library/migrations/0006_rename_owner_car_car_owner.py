# Generated by Django 4.0.1 on 2022-01-06 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_rename_name_owner_first_name_owner_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='owner',
            new_name='car_owner',
        ),
    ]
