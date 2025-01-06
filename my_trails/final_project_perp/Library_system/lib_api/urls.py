from rest_framework.routers import DefaultRouter
from .views import Bookviewset, AuthorViewSet, GenreViewSet

router = DefaultRouter()
router.register(r'book', Bookviewset, basename='book')
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'genres', GenreViewSet, basename='genre')


urlpatterns = router.urls
