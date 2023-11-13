from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('osoby/', views.osoba_list.as_view()),
    path('stanowiska/', views.stanowisko_list),
    path('stanowiska/<int:pk>/', views.stanowisko_detail),
]
