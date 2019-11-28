from django.urls import path

from . import views

urlpatterns = [
        path('', views.index),# designate the vacant url to run the func index in file views.py
        path('rand', views.random_int),# designate the rand url to run the func r_i in file views.py
        path('list/', views.all_pets),
        path('<int:pet_id>', views.pet_details),
        ]
