# Generated by Django 4.2.1 on 2023-08-08 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='image',
            field=models.ImageField(blank=True, upload_to='product-img'),
        ),
    ]
