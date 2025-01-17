# Generated by Django 5.0.6 on 2024-05-28 14:21

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=13)),
                ('surename', models.CharField(max_length=13)),
                ('about', models.TextField()),
                ('image', models.ImageField(upload_to='user_img')),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='KG')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
