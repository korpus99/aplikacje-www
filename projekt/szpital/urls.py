from django.urls import path
from . import views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),
    path('base/', views.base_view, name='base'),
    path('patients/', views.patient_list),
    path('patients/<str:pesel>/', views.patient_detail, name='patient_detail'),
    path('staff/', views.staff_list),
    path('staff/<int:numer_identyfikacyjny>/', views.staff_detail),\
    path('visits/', views.visits_list),
    path('visits_count/<int:pesel>/', views.visits_count),
    path('department_staff/<str:department_name>/', views.staff_in_department, name='staff_in_department'),
]