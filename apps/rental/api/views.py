from django.shortcuts import render
from ..models import Rental
from .serializers import RentalSerializer
from rest_framework import viewsets

# Create your views here.
class RentViewSet(viewsets.ModelViewSet):
    serializer_class = RentalSerializer
    queryset = Rental.objects.all()
