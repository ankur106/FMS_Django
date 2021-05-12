# Generated by Django 3.1.7 on 2021-04-17 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210311_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='productId',
        ),
        migrations.CreateModel(
            name='branch_products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branchId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.branch')),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
    ]