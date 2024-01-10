from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import response

@api_view(['GET'])
def home(request):
    return response.Response({'message': 'Hello World!'})

# Create your views here.
