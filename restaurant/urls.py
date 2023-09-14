from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.MenuItemView.as_view(), name='Hello'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='home')
]
