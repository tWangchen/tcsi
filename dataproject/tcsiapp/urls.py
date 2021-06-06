from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'tcsiapp'

urlpatterns = [
    path('logoutuser', views.logoutuser, name='logoutuser'),
    path('', views.index, name='index'),
    path('tcsielement-csv/', views.downloadcsv, name='tcsielementcsv'),
    path('tcsielement/', views.tcsielement, name='tcsielement'),
]