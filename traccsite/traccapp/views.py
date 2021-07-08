from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template import loader
from .models import WeatherReport

# Create your views here.
def index(request):
    text = 'Hola World!'
    context = {'text': text}
    return render(request, 'traccapp/index.html', context)
#  {'csrfmiddlewaretoken': ['q0cdJW0NPjBPqONvvk0hNjsblpAAtEI1MqfyfyAOHWZFm2KY96erGmCgse4bfFIV'], 'formLoc': ['3'], 'formDate': ['2021-07-10'], 'formTime': ['13:18'], 'sky_cond': ['BKN'], 'wind_dir': ['270'], 'formWindVel': ['22'], 'formTemp': ['2']}
def submit(request):
    weatherReport = WeatherReport()
    weatherReport.location = request.POST['formLoc']
    weatherReport.date = request.POST['formDate']
    weatherReport.time = request.POST['formTime']
    weatherReport.sky_condition = request.POST['sky_cond']
    weatherReport.wind_dir = request.POST['wind_dir']
    weatherReport.wind_vel = request.POST['formWindVel']
    weatherReport.temp = request.POST['formTemp']
    weatherReport.save()


    context = {'weatherReport': weatherReport}
    return render(request, 'traccapp/submit.html', context) 