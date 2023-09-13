from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.sayHello, name='Hello'),
    path('home/', views.home, name='home')
]
