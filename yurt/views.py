from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def business_plan(request):
    return render(request, 'business_plan.html')

def modeldeu (request):
    return render(request, 'modeldeu.html')
def koldanu (request):
    return render(request, 'koldanu.html')

def arduino (request):
    return render(request, 'arduino.html')

def iot (request):
    return render(request, 'iot.html')

def gallery (request):
    return render(request, 'gallery.html')


def iot_view(request):
    return render(request, 'iot.html')

