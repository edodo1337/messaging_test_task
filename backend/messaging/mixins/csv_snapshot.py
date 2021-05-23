from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import renderer_classes
from rest_framework_csv.renderers import CSVRenderer
from messaging.utils import export_messages_to_csv


class MyUserRenderer(CSVRenderer):
    header = ['Title', 'Body', 'Sent', 'Read', 'Created at']


class CsvSnapshot:
    @action(detail=False, methods=['GET', ], permission_classes=[IsAuthenticated])
    @swagger_auto_schema(responses={200: 'Success'}, request=None)
    @renderer_classes((MyUserRenderer,))
    def csv_snapshot(self, request, *args, **kwargs):
        messages = self.filter_queryset(self.get_queryset())
        csv_response = export_messages_to_csv(
            queryset=messages,
            file_name='messages'
        )
        return csv_response
