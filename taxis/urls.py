from django.urls import path
from taxis import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('taxis/', views.taxi_list),
    path('taxis/<int:pk>/', views.taxi_detail),
    path('taxis/<int:taxi_id>/<str:date>/', views.taxi_trayectories, name='taxi-trayectories'),
    path('trayectories/', views.trayectory_list),
    path('trayectories/<int:pk>/', views.trayectory_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)