from django.db import models
from django_resized import ResizedImageField


class Service(models.Model):
    name = models.CharField(max_length=200)
    image = ResizedImageField(size=[1060, 600], force_format='WEBP', quality=75, upload_to='services/')
    description = models.TextField()

    def __str__(self):
        return self.name


class Gallery(models.Model):
    image = ResizedImageField(size=[1060, 600], force_format='WEBP', quality=75, upload_to='gallery/')


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
