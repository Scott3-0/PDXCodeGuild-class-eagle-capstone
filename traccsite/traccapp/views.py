from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    text = 'Hola World!'
    context = {'text': text}
    return render(request, 'traccapp/index.html', context)