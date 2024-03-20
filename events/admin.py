from django.contrib import admin
from .models import Event, RSVP  # Import the RSVP model

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')  
    search_fields = ['title']  
    list_filter = ('date',)  
    prepopulated_fields = {'slug': ('title',)}  

admin.site.register(Event, EventAdmin)  # Register the Event model with the custom admin class
admin.site.register(RSVP)  # Register the RSVP model
