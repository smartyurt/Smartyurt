from django.urls import path
from . import views  # Импортируем views

urlpatterns = [
    path('', views.home, name='home'),
    path('business_plan/', views.business_plan, name='business_plan'),
     path('modeldeu/', views.modeldeu, name='modeldeu'),
    path('koldanu/', views.koldanu, name='koldanu'),
path('arduino/', views.arduino, name='arduino'),
path('iot/', views.iot, name='iot'),
path('gallery/', views.gallery, name='gallery'),
path('iot/', views.iot_view, name='iot'),
]
