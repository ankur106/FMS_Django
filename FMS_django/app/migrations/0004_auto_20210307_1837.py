# Generated by Django 3.0.5 on 2021-03-07 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210307_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbformtype',
            name='fbFormTypeId',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
