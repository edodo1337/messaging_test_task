from users.serializers import RegisterSerializer, LoginSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.utils import swagger_auto_schema
from users.models import User


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

decorated_auth_view = swagger_auto_schema(
    method='post',
    request_body=LoginSerializer
)(obtain_auth_token)