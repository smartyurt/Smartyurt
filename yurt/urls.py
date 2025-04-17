from . import views  # Импортируем views
from django.urls import path
from .views import receive_sensor_data

urlpatterns = [
    path('', views.home, name='home'),
    path('business_plan/', views.business_plan, name='business_plan'),
    path('modeldeu/', views.modeldeu, name='modeldeu'),
    path('koldanu/', views.koldanu, name='koldanu'),
    path('arduino/', views.arduino, name='arduino'),
    path('iot/', views.iot, name='iot'),  # Первый путь для 'iot'
    path('iot_view/', views.iot_view, name='iot_view'),  # Второй путь для 'iot_view' с другим именем
    path('gallery/', views.gallery, name='gallery'),
    path('python_iot/', views.python_iot_view, name='python_iot'),
    path('api/sensor/', receive_sensor_data, name='receive_sensor_data'),
    path('weather_dashboard/', views.weather_dashboard, name='weather_dashboard'),
path('led/', views.led_view, name='led'),
    path('color/', views.color_control, name='color'),
]

