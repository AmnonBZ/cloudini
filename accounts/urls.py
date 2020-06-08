from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', LoginView.as_view(), name="login"),
    path('register/', views.register, name="register"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('update_profile/', views.update_profile, name="update_profile"),
    path('profile/', views.profile, name="profile")
]