from django.contrib import admin
from models import Event
from models import Submission
from models import Speaker
from models import Itinerary

# Register your models here
admin.site.register(Event)
admin.site.register(Submission)
admin.site.register(Speaker)
admin.site.register(Itinerary)
