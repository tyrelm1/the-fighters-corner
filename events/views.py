from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import RSVPForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            attending = form.cleaned_data['attending']
            # Assuming you have a method in your Event model to handle RSVP
            event.update_rsvp_status(request.user, attending)
            return redirect('event_detail', event_id=event_id)
    else:
        form = RSVPForm()
    return render(request, 'events/event_detail.html', {'event': event, 'form': form})
