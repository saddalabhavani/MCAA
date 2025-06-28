from django import forms
from .models import Venue, Event, Participant, Registration

class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'


