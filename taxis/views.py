from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from taxis.models import Taxi
from taxis.serializers import TaxiSerializer

@csrf_exempt
def taxi_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        taxis = Taxi.objects.all()
        serializer = TaxiSerializer(taxis, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaxiSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def taxi_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        taxi = Taxi.objects.get(pk=pk)
    except Taxi.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TaxiSerializer(taxi)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TaxiSerializer(taxi, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        taxi.delete()
        return HttpResponse(status=204)

class CustomPagination(PageNumberPagination):
    page_size = 10  # Número de elementos por página
    page_size_query_param = 'page_size'  # Parámetro para cambiar el tamaño de la página
    max_page_size = 100  # Tamaño máximo de la página permitido