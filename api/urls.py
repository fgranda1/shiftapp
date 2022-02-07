from django.urls import path
from . import views

app_name = 'api'


urlpatterns = [
    path('get_shift', views.get_shift , name='get_shift'),  
    
]