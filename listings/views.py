from rest_framework import generics

from .models import Property
from .serializers import PropertySerializer

class PropertyList(generics.ListAPIView):
    """"
    Get all Properties. 
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyDetail(generics.RetrieveAPIView):
    """
    Get one property by passing in the property ID.
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer