# Generated by Django 2.0.2 on 2018-02-07 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='admin',
            field=models.IntegerField(),
        ),
    ]
