from django.urls import path
from taxis import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('taxis/', views.TaxiList.as_view(), name='taxi-list'),
    path('taxis/<int:pk>/', views.TaxiDetails.as_view(), name='taxi-detail'),
    path('trayectories/', views.TrayectoriesList.as_view()),
    path('trayectories/<int:pk>/', views.TrayectoryDetails.as_view(), name='trayectories'),
]

urlpatterns = format_suffix_patterns(urlpatterns)