#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Pet

def all_pets(request):
    pets = Pet.objects.all()
    context = {
            'pets': pets,
        }
    return render(request, 'adopt/all.html', context)

def pet_details(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    return HttpResponse(pet.name)

import random

def index(request):
    return HttpResponse('Hello')

def random_int(request):
    upper_bound = request.GET.get('ub')
    lower_bound = request.GET.get('lb')
    num = random.randint(int(lower_bound), int(upper_bound))
    return HttpResponse('Your number is: + ' + str(num))
# Create your views here.
