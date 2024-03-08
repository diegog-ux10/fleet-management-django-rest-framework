from datetime import datetime
from django.utils.timezone import make_aware

from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import status

from taxis.serializers import TaxiSerializer, TrayectorySerializer
from taxis.models import Taxi, Trayectory


class TaxiList(ListAPIView):
    """
    List all taxis, or create a new taxi.
    """

    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer


class TaxiDetails(RetrieveAPIView):
    """
    Retrieve, update or delete a code taxis.
    """

    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer


class TrayectoriesList(ListAPIView):
    """
    List all Trayectories, or create a new trayectory.
    """

    serializer_class = TrayectorySerializer

    def get_queryset(self):
        queryset = Trayectory.objects.all()
        taxi_id = self.request.query_params.get("taxi_id", None)
        date = self.request.query_params.get("date", None)

        if taxi_id is not None:
            queryset = queryset.filter(taxi_id=taxi_id)

        if date is not None:
            try:
                date_obj = make_aware(datetime.strptime(date, "%Y-%m-%d"))
                queryset = queryset.filter(
                    date__year=date_obj.year,
                    date__month=date_obj.month,
                    date__day=date_obj.day,
                )
            except ValueError:
                return Response(
                    {"error": "Invalid date format. Use YYYY-MM-DD."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return queryset


class TrayectoryDetails(RetrieveAPIView):
    """
    Retrieve, update or delete a code taxis.
    """

    queryset = Trayectory.objects.all()
    serializer_class = TrayectorySerializer
