from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("home/", views.home, name="home"),
    path('api/menu-items/', views.MenuItemView.as_view(), name='Hello'),
    path('api/menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='home'),
    path('api-token-auth/', obtain_auth_token),
]
