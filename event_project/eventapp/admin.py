from django.contrib import admin
from .models import Organizer, Venue, Event, Participant, Registration

admin.site.register(Organizer)
admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(Participant)
admin.site.register(Registration)



