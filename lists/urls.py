from django.urls import path
from . import views

urlpatterns = [
    path('lists/foobar', views.lists_show),
    path('', views.home_page),
]
