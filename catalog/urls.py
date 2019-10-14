"""Catolog URLs."""

from django.urls import path

from . import views

app_name = "catalog"  # required when using namespace in URLS

urlpatterns = [
    path('', views.mineral_list, name='list'),
    path('list/<name_filter>', views.mineral_list, name='filtered_list'),
    path('detail/<int:pk>/', views.mineral_detail, name='detail'),
    path('import/', views.import_minerals, name='import'),
]
