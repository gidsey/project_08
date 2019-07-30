"""Catolog URLs."""

from django.urls import path

from . import views

app_name = "catalog"  # required when using namespace in URLS

urlpatterns = [
    path('', views.mineral_list, name='list'),
    path('detail/<int:pk>/', views.mineral_detail, name='detail'),
    path('import/', views.import_minerals, name='import'),
    path('import_result/', views.import_result, name='import_result'),
]
