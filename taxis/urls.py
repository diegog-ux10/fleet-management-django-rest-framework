from django.urls import path
from taxis import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('taxis/', views.TaxiList.as_view()),
    path('taxis/<int:pk>/', views.TaxiDetails.as_view()),
    path('trayectories/', views.TrayectoriesList.as_view()),
    path('trayectories/<int:pk>/', views.trayectory_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)