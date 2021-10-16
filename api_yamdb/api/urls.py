from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, CategoryViewSet, TitleViewSet, GenreViewSet

router_v1 = DefaultRouter()
router_v1.register('v1/users', UserViewSet, basename = 'users')
router_v1.register(r'categories', CategoryViewSet)
router_v1.register(r'genres', GenreViewSet)
router_v1.register(r'titles', TitleViewSet)

urlpatterns = [
    path('', include(router_v1.urls)),
]