# Generated by Django 2.0 on 2019-07-25 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_auto_20190725_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(default='static/images/shop/product9.jpg', upload_to='static/images/', verbose_name='My Photo'),
        ),
    ]