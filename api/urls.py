from django.urls import path

from api import views

urlpatterns = [
    path('', views.ApiOverview, name='home')
]
