"""Business view"""

# Django REST Framework
from rest_framework import viewsets

# Serializers
from api.guatudu.serializers import BusinessSerializer

# Models
from api.guatudu.models import Event

class BusinessViewSet(viewsets.ModelViewSet):
    """Tag viewset"""

    queryset = Event.objects.all()
    serializer_class = BusinessSerializer