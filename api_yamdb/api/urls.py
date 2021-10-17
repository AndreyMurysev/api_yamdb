from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (AuthenticationViewSet,
                    admin_putch_get_delete_users,
                    user_putch_get_user,
                    CategoryViewSet,
                    GenreViewSet,
                    LoginView,
                    TitleViewSet,
                    UserViewSet)

router_v1 = DefaultRouter()
router_v1.register('v1/users', UserViewSet, basename='users')
router_v1.register('v1/auth/signup',
                   AuthenticationViewSet,
                   basename='autentication')
router_v1.register(r'v1/categories', CategoryViewSet)
router_v1.register(r'v1/genres', GenreViewSet)
router_v1.register(r'v1/titles', TitleViewSet)

urlpatterns = [
    path('v1/auth/token/',
         LoginView.as_view(),
         name='token_obtain_pair'),
    path('v1/users/me/', user_putch_get_user, name='me'),
    path(
        'v1/users/<slug:username>/',
        admin_putch_get_delete_users,
        name='username'),
    path('', include(router_v1.urls)),
]
