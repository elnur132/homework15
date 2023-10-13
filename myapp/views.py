from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
cars = ['audi', 'geely', 'honda']
def index(request):
    return JsonResponse(cars, safe=False)