from django.urls import path
from taxis import views

urlpatterns = [
    path('taxis/', views.taxi_list),
    path('taxis/<int:pk>/', views.taxi_detail),
]