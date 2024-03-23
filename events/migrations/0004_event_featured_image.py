# Generated by Django 4.2.11 on 2024-03-23 00:33

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_remove_event_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
