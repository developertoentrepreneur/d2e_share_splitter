# Generated by Django 3.2.9 on 2021-11-26 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContribLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(default='creation', max_length=1024)),
                ('user', models.CharField(max_length=1024)),
                ('details', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=1024)),
                ('contribType', models.CharField(max_length=1024)),
                ('projectType', models.CharField(max_length=1024)),
                ('value', models.FloatField(default=0)),
                ('hours', models.FloatField()),
                ('date', models.DateField()),
                ('details', models.CharField(max_length=1024)),
                ('slices', models.FloatField(default=0)),
            ],
        ),
    ]
