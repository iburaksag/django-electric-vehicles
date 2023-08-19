from django.urls import path

from config import views
from core.views import home_view

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', home_view, name="home"),  
]
