# Generated by Django 4.0.1 on 2022-05-05 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_product_image_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', null=True, upload_to='images'),
        ),
    ]
