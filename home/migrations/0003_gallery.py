# Generated by Django 5.0.1 on 2024-01-30 18:00

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[1060, 600], upload_to='gallery/')),
            ],
        ),
    ]
