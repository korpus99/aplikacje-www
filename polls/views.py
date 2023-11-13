from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Osoba, Stanowisko
from .serializers import OsobaSerializer, StanowiskoSerializer

def index(request):
    return HttpResponse("Hello World. You are at the poll index.")

@api_view(['GET'])
def stanowisko_list(request):
    if request.method == 'GET':
        stanowiska = Stanowisko.objects.all()
        serializer = StanowiskoSerializer(stanowiska, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def stanowisko_detail(request, pk):
    try:
        stanowisko = Stanowisko.objects.get(pk=pk)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        stanowisko = Stanowisko.objects.get(pk=pk)
        serializer = StanowiskoSerializer(stanowisko)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StanowiskoSerializer(stanowisko, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stanowisko.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class osoba_list(APIView):
    def get(self, request, format=None):
        osoby = Osoba.objects.all()
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)
