from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('brform/', views.BRform, name='BR-form'),
    # path('<str>/', views.brformsubmitted, name='BR-form-submitted-get'),
    # path('<str>/', views.brformsubmitted, name='BR-form-submitted-get'),
]