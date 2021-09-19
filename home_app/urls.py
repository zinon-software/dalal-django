from django.urls import path, include
from rest_framework import routers
from . import api
from rest_framework.authtoken.views import obtain_auth_token


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', api.UserViewSet)

urlpatterns = [
    path('hello/', api.HelloView.as_view(), name='hello'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]