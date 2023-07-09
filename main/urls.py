from django.contrib import admin
from django.urls import path

from .views import index, result, ESE, ESH, ENE, ENH, ISE, ISH, INE, INH

app_name = 'main'

urlpatterns = [
    path('', index, name='index_2'),
    path('result/', result, name='result'),
    path('result/ESE/', ESE),
    path('result/ESH/', ESH),
    path('result/ENE/', ENE),
    path('result/ENH/', ENH),
    path('result/ISE/', ISE),
    path('result/ISH/', ISH),
    path('result/INE/', INE),
    path('result/INH/', INH),
]