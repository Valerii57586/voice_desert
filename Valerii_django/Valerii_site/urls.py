from django.urls import path
from . import views

app_name = 'Valerii_site'

urlpatterns = [
    path('', views.index),
    # path('Valerii_django/', views.all_site)
]