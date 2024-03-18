from django.contrib import admin
from .models import Event, RSVP

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')  
    search_fields = ['title']  
    list_filter = ('date',)  
    prepopulated_fields = {'slug': ('title',)}  

admin.site.register(Event)
admin.site.register(RSVP)