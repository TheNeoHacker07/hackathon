# Generated by Django 5.0.6 on 2024-05-28 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='telephone',
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='user_img'),
        ),
    ]
