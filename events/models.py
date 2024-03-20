from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class RSVP(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rsvp_status = models.BooleanField(default=False)  # True for attending, False for not attending

    def update_rsvp_status(self, rsvp_status):
        # Update the RSVP status for this user and event
        self.rsvp_status = rsvp_status
        self.save()
