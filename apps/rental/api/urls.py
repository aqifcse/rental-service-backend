from apps.rental.api import views

from django.urls import path

urlpatterns = [
    path('rents/', views.RentViewSet.as_view({'get': 'list'}), name='rents'),
    path('searchRentalInfo/<str:q>', views.SearchRentalInfoAPIView.as_view())
]