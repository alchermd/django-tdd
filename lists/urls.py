from django.urls import path
from . import views

urlpatterns = [
    path('lists/<int:list_id>/add_task', views.lists_add_task),
    path('lists/<int:list_id>', views.lists_show),
    path('', views.home_page),
]
