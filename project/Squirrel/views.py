from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count, Q

from .models import Squirrel

def index(request):
    return render(request, 'Squirrel/index.html')

def sightings(request):
    squirrel_id = list()
    for i in Squirrel.objects.all():
        i_dict = {}
        i_dict['sid']=i.squirrel_id
        squirrel_id.append(i_dict)
    return render(request, 'Squirrel/sightings.html', {'squirrel_id':squirrel_id})
