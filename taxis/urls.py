from django.urls import path
from taxis import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('taxis/', views.taxi_list),
    path('taxis/<int:pk>/', views.taxi_detail),
    path('trayectories/<int:taxi_id>/<str:date>/', views.trayectories_list),
    path('trayectories/<int:pk>/', views.trayectory_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)