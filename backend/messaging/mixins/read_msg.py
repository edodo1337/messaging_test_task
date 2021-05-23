from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated


class ReadMsgMixin:
    @action(detail=True, methods=['POST', ], permission_classes=[IsAuthenticated])
    @swagger_auto_schema(responses={200: 'Success'}, request=None)
    def mark_read(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.mark_read()
            return Response({'status': True}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            