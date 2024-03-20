from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Event, RSVP
from .forms import RSVPForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    
    # Check if the current user has already RSVP'd for this event
    rsvp, created = RSVP.objects.get_or_create(event=event, user=request.user)
    
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            attending = form.cleaned_data['attending']
            # Update the RSVP status
            rsvp.rsvp_status = attending
            rsvp.save()
            # Add a success message
            messages.success(request, 'Your RSVP has been confirmed!')
            # Redirect to the event list page or any other desired page
            return redirect('event_list')  # Change 'event_list' to the appropriate URL name
    else:
        # Initialize the RSVP form with the existing RSVP status or None if it doesn't exist
        initial_data = {'attending': rsvp.rsvp_status if rsvp else None}
        form = RSVPForm(initial=initial_data)
        
    return render(request, 'events/event_detail.html', {'event': event, 'form': form})
