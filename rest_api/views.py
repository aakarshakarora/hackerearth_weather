from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Record
from .serializers import RecordSerializer


class RecordViewSetWithOptions(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    @action(detail=False, methods=['GET'])
    def get_weather_records(self, request):
        date_param = request.query_params.get('date', None)
        city_param = request.query_params.get('city', None)
        sort_param = request.query_params.get('sort', None)

        records = self.queryset

        if date_param:
            records = records.filter(date=date_param)

        if city_param:
            records = records.filter(city__iexact=city_param)

        if sort_param == 'date':
            records = records.order_by('date', 'id')
        elif sort_param == 'date_desc':
            records = records.order_by('-date', 'id')

        serializer = RecordSerializer(records, many=True)
        return Response(serializer.data, status=200)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def perform_create(self, serializer):

        serializer.save()
