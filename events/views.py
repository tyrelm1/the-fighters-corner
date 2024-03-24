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

    rsvp, created = RSVP.objects.get_or_create(event=event, user=request.user)
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            attending = form.cleaned_data['attending']
            rsvp.rsvp_status = attending
            rsvp.save()
            messages.success(request, 'Your RSVP has been confirmed!')

            return redirect('event_list')
    else:

        initial_data = {'attending': rsvp.rsvp_status if rsvp else None}
        form = RSVPForm(initial=initial_data)

    return render(request, 'events/event_detail.html', {'event': event, 'form': form})
