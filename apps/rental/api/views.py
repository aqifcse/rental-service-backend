from django.shortcuts import render
from ..models import Rental
from .serializers import RentalSerializer
from rest_framework import viewsets, generics
from rest_framework import filters

# Create your views here.
class RentViewSet(viewsets.ModelViewSet):
    serializer_class = RentalSerializer
    queryset = Rental.objects.all()

class SearchRentalInfoAPIView(generics.ListCreateAPIView):
    search_fields = ['name', 'code', 'type']
    filter_backends = (filters.SearchFilter,)
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    