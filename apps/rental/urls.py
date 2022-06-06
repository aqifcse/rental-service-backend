from apps.rental.views import MovieViewSet
from rest_framework.routers import DefaultRouter
from apps.rental import views

router = DefaultRouter()
router.register(r'movies', views.MovieViewSet, basename='movie')
urlpatterns = router.urls