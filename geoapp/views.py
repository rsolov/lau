from .models import Marker
from .serializers import MarkerSerializer
from rest_framework.renderers import JSONRenderer
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import render



@csrf_exempt
def marker_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        marker = Marker.objects.all()
        serializer = MarkerSerializer(marker, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MarkerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def home(request):
    marker = Marker.objects.all()
    return render(request, 'home.html', {'marker': marker})
