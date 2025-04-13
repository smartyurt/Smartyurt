from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import SensorData

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
def python_iot_view(request):
    return render(request, 'python_iot.html')

def weather_dashboard(request):
    data = SensorData.objects.order_by('-timestamp')[:10]
    return render(request, 'weather_dashboard.html', {'data': data})



@csrf_exempt
def receive_sensor_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            temperature = data.get('temperature')
            humidity = data.get('humidity')

            if temperature is not None and humidity is not None:
                SensorData.objects.create(temperature=temperature, humidity=humidity)
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Missing fields'}, status=400)
        except:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)


