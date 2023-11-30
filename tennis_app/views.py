from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


def mi_vista(request):
    context = {'STATIC_URL': settings.STATIC_URL}
    return render(request, 'tennis_app/index.html', context)

