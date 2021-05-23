from rest_framework import routers
from messaging.views import MessagingViewSet
from django.urls import include, path
from django.conf.urls import url

messaging_router = routers.DefaultRouter()
messaging_router.register(r'', MessagingViewSet, basename='messaging')


messaging_urlpatterns = []
messaging_urlpatterns += messaging_router.urls


