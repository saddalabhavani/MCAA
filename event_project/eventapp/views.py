from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event, Venue, Participant, Registration, Organizer
from .forms import EventForm, VenueForm, ParticipantForm, RegistrationForm
from django.db.models import Count
# Event List View
@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

# Create Event
@login_required
def event_create(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('event_list')
    return render(request, 'event_form.html', {'form': form})

# Edit Event
@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('event_list')
    return render(request, 'event_form.html', {'form': form})

# Delete Event
@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'confirm_delete.html', {'object': event, 'type': 'Event'})

# Register Participant
@login_required
def register_participant(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('event_list')
    return render(request, 'registration_form.html', {'form': form})

# Show Registrations
@login_required
def registration_list(request):
    registrations = Registration.objects.select_related('participant', 'event')
    return render(request, 'registration_list.html', {'registrations': registrations})

@login_required
def registration_report(request):
    events = Event.objects.all()
    selected_event_id = request.GET.get('event')
    
    if selected_event_id:
        registrations = Registration.objects.filter(event_id=selected_event_id)
    else:
        registrations = Registration.objects.all()
        
    return render(request, 'registration_report.html', {
        'events': events,
        'registrations': registrations,
        'selected_event_id': selected_event_id,
    })


