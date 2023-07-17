from django.urls import path
from . import views

app_name = 'Valerii_site'
print(1)

urlpatterns = [
    path('', views.index),
    path('Valerii_django/', views.all_site),
    path('site/<pk>', views.only_site),
]