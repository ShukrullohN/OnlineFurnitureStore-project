# Generated by Django 5.0.4 on 2024-05-31 12:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_productmodel_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='discount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
