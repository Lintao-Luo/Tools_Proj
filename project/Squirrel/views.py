from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count, Q
from .forms import SquirrelForm
from .models import Squirrel
import random

def index(request):
    return render(request, 'Squirrel/index.html')

def sightings(request):
    squirrel_id = list()
    for i in Squirrel.objects.all():
        i_dict = {}
        i_dict['sid']=i.squirrel_id
        squirrel_id.append(i_dict)
    return render(request, 'Squirrel/sightings.html', {'squirrel_id':squirrel_id})

def add(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/Squirrel/sightings')

    else:
        form = SquirrelForm()

    context = {
            'form': form,
    }

    return render(request, 'Squirrel/add.html', context)


def get_map(request):
    sightings = random.sample(list(Squirrel.objects.all()), 100)
    return render(request, 'Squirrel/map.html', {'sightings':sightings})

def update(request, squirrel_id):
    squirrel = Squirrel.objects.get(squirrel_id=squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/Squirrel/sightings/')

    else:
        form = SquirrelForm(instance=squirrel)

    context = {
            'form': form,
    }

    return render(request, 'Squirrel/add.html', context)

def get_stats(request):
    total_num = Squirrel.objects.all().count()
    s1_adult_rate = Squirrel.objects.filter(age='Adult').count()/total_num
    s2_ground_plane_rate = Squirrel.objects.filter(location='Ground Plane').count()/total_num
    s3_running_rate = Squirrel.objects.filter(running=True).count()/total_num
    s4_chasing_rate = Squirrel.objects.filter(chasing=True).count()/total_num
    s5_eating_rate = Squirrel.objects.filter(eating=True).count()/total_num
    stats_dict = {'s1':s1_adult_rate, 's2':s2_ground_plane_rate, 's3':s3_running_rate, 's4':s4_chasing_rate, 's5':s5_eating_rate}
    return render(request, 'Squirrel/stats.html', stats_dict)

