# Generated by Django 2.0 on 2019-07-25 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_auto_20190725_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=100, max_length=100),
        ),
    ]
