from django.http import HttpResponse
from django.shortcuts import render


def mi_vista(request):
    return render(request, 'tennis_app/index.html')

