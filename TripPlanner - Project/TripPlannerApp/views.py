from rest_framework import viewsets
from TripPlannerApp.serializers import TripSerializer
from TripPlannerApp.models import Trip


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
