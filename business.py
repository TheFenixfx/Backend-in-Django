"""Business Serializer"""

#Django Rest Framework
from rest_framework import serializers
#Model
from api.guatudu.models import Business
# from api.guatudu.serializers import AdminProfilesSerializer

class BusinessSerializer(serializers.ModelSerializer):
    """Business Model Serializer"""
    # admin_profiles = AdminProfilesSerializer(read_only=True)
    class Meta:
        """Meta class"""
        model = Business
        fields = (
            'id',
            'name',
            'image',
            'phone_number',
            'email',
            'rating',
            'description',
        )
