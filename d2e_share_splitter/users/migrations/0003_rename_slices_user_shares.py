# Generated by Django 3.2.9 on 2022-01-07 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211206_1844'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='slices',
            new_name='shares',
        ),
    ]