from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, RSVP
from .forms import RSVPForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

from django.contrib import messages

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    
    # Check if the current user has already RSVP'd for this event
    rsvp = RSVP.objects.filter(event=event, user=request.user).first()
    
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            attending = form.cleaned_data['attending']
            # If the user has already RSVP'd, update the existing RSVP object
            if rsvp:
                rsvp.rsvp_status = attending
                rsvp.save()
            else:
                # If the user hasn't RSVP'd yet, create a new RSVP object
                RSVP.objects.create(event=event, user=request.user, rsvp_status=attending)
            # Add a success message
            messages.success(request, 'Your RSVP has been confirmed!')
            return redirect('event_detail', event_id=event_id)
    else:
        initial_data = {'attending': rsvp.rsvp_status if rsvp else None} if rsvp else {}
        form = RSVPForm(initial=initial_data)
        
    return render(request, 'events/event_detail.html', {'event': event, 'form': form})
