
from myapp.models import Car

def cars(request):
    cars = Car.objects.all()
    return {'cars': cars}