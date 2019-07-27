"""Catolog URLs."""

from django.urls import path

from . import views

app_name = "catalog"  # required when using namespace in URLS

urlpatterns = [
    path('', views.mineral_list, name='list'),
    path('detail/', views.mineral_detail, name='detail')
]
