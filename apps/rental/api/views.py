from django.shortcuts import render
from ..models import Rental
from .serializers import RentalSerializer
from rest_framework import viewsets, generics

# Create your views here.
class RentViewSet(viewsets.ModelViewSet):
    serializer_class = RentalSerializer
    queryset = Rental.objects.all()

class SearchRentalInfoAPIView(generics.ListCreateAPIView):
    serializer_class = RentalSerializer
    def search(request):
        query = request.GET.get("q")  
        if query:
            queryset = Rental.objects.filter(
                Q(name=query)|   
                Q(code=query)|
                Q(type=query)
                ).distinct()
