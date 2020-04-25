from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('view_policies', views.view_policies, name='view_policies'),
    path('my_policies', views.my_policies, name='my_policies'),
    path('violations', views.violations, name='violations'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
]
