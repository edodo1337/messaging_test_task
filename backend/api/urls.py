from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from messaging.routers import messaging_urlpatterns
from users.views import RegisterView, decorated_auth_view


schema_view = get_swagger_view('API Documentation')

schema_view = get_schema_view(
    openapi.Info(
        title="Messaging API",
        default_version='v1',
    ),
    validators=['ssv', 'flex'],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^swagger(?P<format>.json|.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^$', schema_view),
    url('messaging/', include(messaging_urlpatterns)),
    url('auth/', decorated_auth_view, name='api_token_auth'),
    url('register/', RegisterView.as_view(), name='auth_register'),
]