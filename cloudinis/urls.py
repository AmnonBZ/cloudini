from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('policies', views.policies, name='policies'),
    path('violations', views.violations, name='violations'),
    path('scan', views.scan, name='scan'),
]
