from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify  # Import slugify function

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)  # Add slug field

    def save(self, *args, **kwargs):
        # Generate slug automatically from the title if it's not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class RSVP(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rsvp_status = models.BooleanField(default=False)  # True for attending, False for not attending

