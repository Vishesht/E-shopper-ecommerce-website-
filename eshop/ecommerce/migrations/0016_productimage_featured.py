# Generated by Django 2.0 on 2019-08-01 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0015_auto_20190801_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]