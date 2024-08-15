

from django.urls import path

from .api_views import  LoginAPIView, LogoutAPIView, ProductListCreateView, RegisterAPIView
from . import views

urlpatterns = [
  path('',views.home,name='home'),
  path('about/',views.about,name='about'),
  path('login/',views.login_user,name='login'),
  path('logout/',views.logout_user,name='logout'),
  path('register/',views.register_user,name='register'),


   # API URLs
    path('api/products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('api/register/', RegisterAPIView.as_view(), name='api-register'),
    path('api/login/', LoginAPIView.as_view(), name='api-login'),
    path('api/logout/', LogoutAPIView.as_view(), name='api-logout'),
]
