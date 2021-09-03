from django.urls import path
from main import views

urlpatterns = [
    path('', views.Home.as_view(), name='Home'),
]

