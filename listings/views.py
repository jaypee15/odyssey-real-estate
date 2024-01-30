from rest_framework import generics

from .models import Property
from .serializers import PropertySerializer

class PropertyList(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyDetail(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer