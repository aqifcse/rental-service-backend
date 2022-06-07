from apps.rental.api.views import RentViewSet
from rest_framework.routers import DefaultRouter
from apps.rental.api import views

router = DefaultRouter()
router.register(r'rents', views.RentViewSet, basename='rent')
urlpatterns = router.urls