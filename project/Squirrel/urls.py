from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('sightings/', views.sightings, name='sightings'),
    path('sightings/add', views.add, name='add'),
    path('sightings/<str:squirrel_id>/', views.update, name='update'),
    path('map/', views.get_map, name='map'),
    path('sightings/stats', views.get_stats, name='stats'),
]
