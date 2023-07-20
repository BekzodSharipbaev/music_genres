from django.http import HttpRequest
from django.shortcuts import render

from .models import Singer

# Create your views here.
def show_singers(request:HttpRequest):
    singers = Singer.objects.all()
    context = {"singers": singers, "category": "Pop"}
    return render(request, 'singers.html', context)

def show_singer(request:HttpRequest, slug:str):
    singer = Singer.objects.get(slug=slug)
    context = {"singer": singer}
    return render(request, 'singer.html', context)


