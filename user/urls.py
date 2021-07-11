from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('fan-sign-up/', views.fan_sign_up, name='fan-sign-up'),
    path('talent-sign-up/', views.talent_sign_up, name='talent-sign-up')
]