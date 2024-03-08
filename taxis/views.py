# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from taxis.models import Taxi, Trayectory
from taxis.serializers import TaxiSerializer, TrayectorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

@api_view(['GET', 'POST'])
def taxi_list(request, format=None):
    """
    List all code taxis, or create a new taxi.
    """
    if request.method == 'GET':
        taxis = Taxi.objects.all()
        serializer = TaxiSerializer(taxis, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaxiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def taxi_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code taxis.
    """
    try:
        taxi = Taxi.objects.get(pk=pk)
    except Taxi.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaxiSerializer(taxi)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaxiSerializer(taxi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        taxi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def trayectories_list(request, taxi_id, date, format=None):
    """
    Retrieve trayectories of a taxi for a given date.
    """
    print(request)
    try:
        trayectories = Trayectory.objects.filter(taxi_id=taxi_id, date__date=date)
        serializer = TrayectorySerializer(trayectories, many=True)
        return Response(serializer.data)
    except Trayectory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'PUT', 'DELETE'])
def trayectory_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code trayectories.
    """
    try:
        trayectory = Trayectory.objects.get(pk=pk)
    except Trayectory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TrayectorySerializer(trayectory)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TrayectorySerializer(trayectory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        trayectory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class CustomPagination(PageNumberPagination):
#     page_size = 10  # Número de elementos por página
#     page_size_query_param = 'page_size'  # Parámetro para cambiar el tamaño de la página
#     max_page_size = 100  # Tamaño máximo de la página permitido