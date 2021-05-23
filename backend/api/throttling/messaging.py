from re import U
from typing import overload
from rest_framework import throttling
from django.core.cache import caches
from django.utils import timezone
from users.models import User
from users.utils import get_client_ip
from app.settings.logger_setup import configure_logger

# import logging
# logger = logging.getLogger(__name__)


logger = configure_logger('messaging')


class MessagingRateThrottle(throttling.ScopedRateThrottle):
    cache = caches['default']
    scope = 'messaging'

    def allow_request(self, request, view):
        if request.method != 'POST':
            return True

        allowed = super().allow_request(request, view)
        ip = get_client_ip(request)

        overload_requests = self.cache.get(f'{ip}_overload', 0)

        if not allowed:
            if self.timer() - self.history[0] > 1.0:
                if overload_requests > 5:
                    user = User.objects.filter(ip=ip).first()
                    if user is not None:
                        user.is_active = False
                        user.banned_at = timezone.datetime.now()
                        user.save()
                        logger.debug(f'Banned client: {user.ip}')
                self.cache.set(f'{ip}_overload', overload_requests + 1)
        else:
            self.cache.set(f'{ip}_overload', 0)

        return allowed
    