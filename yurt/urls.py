
from . import views  # Импортируем views
from django.urls import path
from .views import receive_sensor_data
urlpatterns = [
    path('', views.home, name='home'),
    path('business_plan/', views.business_plan, name='business_plan'),
     path('modeldeu/', views.modeldeu, name='modeldeu'),
    path('koldanu/', views.koldanu, name='koldanu'),
path('arduino/', views.arduino, name='arduino'),
path('iot/', views.iot, name='iot'),
path('gallery/', views.gallery, name='gallery'),
path('iot/', views.iot_view, name='iot'),
path('api/sensor/', receive_sensor_data, name='receive_sensor_data'),
    path('weather_dashboard/', views.weather_dashboard, name='weather_dashboard'),
]
