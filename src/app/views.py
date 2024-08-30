from django.http import HttpResponse
from django.shortcuts import render
from app.tasks import download_cat

# Create your views here.
def index(request):
    download_cat.delay()
    return HttpResponse('Грузим котика')