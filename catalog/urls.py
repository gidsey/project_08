"""Catolog URLs."""

from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path('', views.check_data, name='check_data'),
    path('list/', views.mineral_list, name='list'),
    path('list/letter/<name_filter>', views.mineral_list, name='filtered_list'),
    path('list/group/<group_filter>', views.mineral_group, name='group_list'),
    path('list/streak/<streak_filter>', views.mineral_streak, name='streak_list'),
    path('detail/<int:pk>/', views.mineral_detail, name='detail'),
    path('import/', views.import_minerals, name='import'),
    path('search/', views.search, name='search'),
]
