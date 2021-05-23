from drf_yasg import views
from rest_framework import permissions
from django.utils import timezone
from datetime import timedelta
from users.models import User
from users.utils import get_client_ip
from rest_framework.exceptions import APIException
from rest_framework import status


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    pass


def user_is_banned(ip: str) -> bool:
    user = User.objects.filter(ip=ip).first()
    if user is not None:
        if not user.is_active:
            if timezone.datetime.now() - user.banned_at > timedelta(minutes=10):
                user.is_active = True
                user.save()
        return not user.is_active
    else:
        return True


class BannedForbidden(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "You are banned for 10 minutes."


class MessagingAccessPermission(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        banned = False
        if view.action == 'create' and request.user.is_authenticated:
            ip = get_client_ip(request)
            banned = user_is_banned(ip)
            if banned:
                raise BannedForbidden

        return super().has_permission(request, view) 

