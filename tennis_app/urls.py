# En tu_app/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('index', views.mi_vista, name='nombre_de_la_vista'),
]
