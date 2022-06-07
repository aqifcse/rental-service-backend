from apps.rental.api.views import MovieViewSet
from rest_framework.routers import DefaultRouter
from apps.rental.api import views

router = DefaultRouter()
router.register(r'movies', views.MovieViewSet, basename='movie')
urlpatterns = router.urls