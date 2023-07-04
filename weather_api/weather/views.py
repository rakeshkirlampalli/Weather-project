from rest_framework import viewsets
from .models import Weather
from .serializers import WeatherSerializer

class WeatherViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Weather.objects.all()
    serializer_class


# Create your views here.
