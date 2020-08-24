"""Events view"""

# Django REST Framework
from rest_framework import viewsets

# Serializers
from api.guatudu.serializers import EventSerializer

# Models
from api.guatudu.models import Event

class EventViewSet(viewsets.ModelViewSet):
    """Event viewset"""

    queryset = Event.objects.all()
    serializer_class = EventSerializer