# Generated by Django 4.2.11 on 2024-03-23 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_featured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='featured_image',
        ),
    ]
