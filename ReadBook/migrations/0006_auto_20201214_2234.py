# Generated by Django 3.1.1 on 2020-12-14 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReadBook', '0005_auto_20201214_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(default='default/no_cover.jpg', null=True, upload_to='book_images/'),
        ),
    ]
