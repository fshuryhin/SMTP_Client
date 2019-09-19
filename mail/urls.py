from django.urls import path
from . import views

app_name = 'mail'
urlpatterns = [
    path('', views.index, name='index'),
    path('send/', views.sendMail, name='send'),
    path('settings/', views.setSettings, name='settings'),
]