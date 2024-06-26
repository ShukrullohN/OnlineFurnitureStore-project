# Generated by Django 5.0.4 on 2024-06-07 10:15

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_productmodel_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductManufacture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='manufacture/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Product Manufacture',
                'verbose_name_plural': 'Product Manufactures',
            },
        ),
        migrations.AlterModelOptions(
            name='productcategorymodel',
            options={'verbose_name': 'Product Category', 'verbose_name_plural': 'Product Categories'},
        ),
        migrations.AlterModelOptions(
            name='productcolormodel',
            options={'verbose_name': 'Product Color', 'verbose_name_plural': 'Product Colors'},
        ),
        migrations.AlterModelOptions(
            name='productimagemodel',
            options={'verbose_name': 'image', 'verbose_name_plural': 'images'},
        ),
        migrations.AlterModelOptions(
            name='productsizemodel',
            options={'verbose_name': 'Product Size', 'verbose_name_plural': 'Product Sizes'},
        ),
        migrations.AlterModelOptions(
            name='producttagmodel',
            options={'verbose_name': 'Product Tag', 'verbose_name_plural': 'Product Tags'},
        ),
        migrations.RenameField(
            model_name='productmodel',
            old_name='image',
            new_name='image2',
        ),
        migrations.RenameField(
            model_name='productmodel',
            old_name='description',
            new_name='long_description',
        ),
        migrations.RenameField(
            model_name='productmodel',
            old_name='size',
            new_name='sizes',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='short_info',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='real_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='short_description',
            field=models.CharField(default='qwe456yuisdfghj', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productimagemodel',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.productmodel'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='count',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='discount',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='image1',
            field=models.ImageField(upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='sku',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='tags',
            field=models.ManyToManyField(related_name='products', to='products.producttagmodel'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='manufacture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.productmanufacture'),
        ),
        migrations.DeleteModel(
            name='ProductManufactureModel',
        ),
    ]
