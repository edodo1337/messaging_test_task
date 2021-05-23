from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from messaging.serializers import MessageDetailSerializer, MessageCreateSerializer, MessageUpdateSerializer
from messaging.models import Message
from messaging.mixins import ReadMsgMixin, CsvSnapshot
from django_filters.rest_framework import DjangoFilterBackend
from api.throttling.messaging import MessagingRateThrottle
from messaging.permissions.messaging import MessagingAccessPermission
from rest_framework.authentication import TokenAuthentication


class MessagingViewSet(viewsets.ModelViewSet, ReadMsgMixin, CsvSnapshot):
    authentication_classes = [TokenAuthentication]
    permission_classes = (MessagingAccessPermission,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'title', 'body', 'flag_sent', 'flag_read',]
    throttle_scope = 'messaging'
    throttle_classes = [MessagingRateThrottle]
    queryset = Message.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action == 'list':
            return MessageDetailSerializer
        if self.action == 'retrieve':
            return MessageDetailSerializer
        if self.action == 'create':
            return MessageCreateSerializer
        if self.action == 'update':
            return MessageUpdateSerializer
        if self.action == 'mark_read':
            return None
        return MessageDetailSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_permissions(self):
        return super(MessagingViewSet, self).get_permissions()

    def get_serializer_context(self):
        context = super(MessagingViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context

    def perform_create(self, serializer):
        serializer.save()
