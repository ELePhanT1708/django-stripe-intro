# Generated by Django 3.2.6 on 2022-11-24 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, upload_to='product/static/product', verbose_name='Фото'),
        ),
    ]
