# Generated by Django 4.2.1 on 2023-08-09 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='../upload/Education Logo.png', null=True, upload_to=''),
        ),
    ]
