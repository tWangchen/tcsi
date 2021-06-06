from tcsiapp.views import tcsielement
from django.conf.urls import url 
from django.urls import path, include
from .views import(
    TcsiElementApiView
)

app_name = 'tcsiapi'

urlpatterns = [
    path('tcsielements/', TcsiElementApiView.as_view(), name='tcsielementapi'),
]