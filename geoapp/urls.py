
from django.urls import path
from geoapp import views

urlpatterns = [
    path('api/marker/', views.marker_list),
    path('', views.home),
]
