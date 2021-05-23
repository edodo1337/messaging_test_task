from celery.utils.imports import instantiate
from rest_framework import serializers, validators
from messaging.models import Message
from messaging.celery_tasks import send_message
from users.utils import get_client_ip
from users.models import User


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from messaging.models import Message


class MessageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('title', 'body',)
    
    def create(self, validated_data):
        ip = self.context.get('ip', None)

        user = None
        # if ip is not None:
        #     user = User.objects.get_or_create(ip=ip)

        request = self.context.get('request')
        if request is not None and request.user.is_authenticated:
            user = request.user

        instance: Message = super().create(validated_data)
        instance.user = user
        instance.save()

        send_message.apply_async(args=(instance.pk,))
        return instance

class MessageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('title', 'body',)