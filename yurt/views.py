
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import SensorData

from django.shortcuts import redirect, render
import requests

ESP8266_IP = "http://192.168.0.123"  # Замените на IP вашего ESP

def color_control(request):
    color = request.GET.get("color")
    if color == "red":
        requests.get(f"{ESP8266_IP}/color?r=1023&g=0&b=0")
    elif color == "blue":
        requests.get(f"{ESP8266_IP}/color?r=0&g=0&b=1023")
    elif color == "off":
        requests.get(f"{ESP8266_IP}/color?r=0&g=0&b=0")

    return redirect("home")

def home(request):
    return render(request, "home.html")



def home(request):
    return render(request, 'home.html')


def business_plan(request):
    return render(request, 'business_plan.html')


def modeldeu(request):
    return render(request, 'modeldeu.html')


def koldanu(request):
    return render(request, 'koldanu.html')


def arduino(request):
    return render(request, 'arduino.html')


def iot(request):
    return render(request, 'iot.html')


def gallery(request):
    return render(request, 'gallery.html')


def iot_view(request):
    return render(request, 'iot.html')


def python_iot_view(request):
    return render(request, 'python_iot.html')
def led_view(request):
    return render(request, 'led.html')


def weather_dashboard(request):
    data = SensorData.objects.order_by('-timestamp')[:10]
    return render(request, 'weather_dashboard.html', {'data': data})


@csrf_exempt
def receive_sensor_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Извлекаем данные из запроса
            temperature = data.get('temperature')
            humidity = data.get('humidity')
            gas_concentration = data.get('gas_concentration')  # Добавлено для концентрации газа
            gas_type = data.get('gas_type', 'methane')  # Если тип газа не указан, по умолчанию метан
            sensor_id = data.get('sensor_id', None)  # Добавляем sensor_id, если он есть

            # Проверка наличия необходимых полей
            if temperature is not None and humidity is not None and gas_concentration is not None:
                # Сохраняем данные в базе
                SensorData.objects.create(
                    temperature=temperature,
                    humidity=humidity,
                    gas_concentration=gas_concentration,
                    gas_type=gas_type,
                    sensor_id=sensor_id  # Передаём sensor_id
                )
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Missing fields'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)

