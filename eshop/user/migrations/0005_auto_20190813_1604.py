# Generated by Django 2.0 on 2019-08-13 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190813_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(default=1, upload_to='profile_pics'),
            preserve_default=False,
        ),
    ]
