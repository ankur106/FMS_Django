# Generated by Django 3.0.5 on 2021-03-07 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FBFormType',
            fields=[
                ('fbFormTypeId', models.AutoField(primary_key=True, serialize=False)),
                ('fbFormTypeName', models.CharField(max_length=40)),
            ],
        ),
    ]
