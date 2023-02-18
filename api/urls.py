from django.urls import path

from api import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_item, name='add-item'),
    path('all/', views.view_items, name='view-items'),
    path('update/<int:pk>', views.update_item, name='update-item'),
]
