from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    PolicyListView,
    PolicyCreateView,
    PolicyDeleteView,
    PolicyUpdateView,
)

urlpatterns = [
    path('', views.home, name='home'),
    # path('profile', views.profile, name='profile'),
    # path('profile/<int:pk>/update/', UserUpdateView.as_view(), name='profile'),
    path('about', views.about, name='about'),
    #path('policies', views.policies, name='policies'),
    path('view_policies', views.view_policies, name='view_policies'),
   # path('new_policy', views.new_policy, name='new_policy'),
    path('violations', views.violations, name='violations'),
    path('scan', views.scan, name='scan'),
    path('new_policy', PolicyCreateView.as_view(), name='new_policy'),
    path('policies', PolicyListView.as_view(), name='policies'),
    path('policies/<int:pk>/delete/', PolicyDeleteView.as_view(), name='delete_policy'),
    path('policies/<int:pk>/update/', PolicyUpdateView.as_view(), name='update_policy'),

    path('login/', LoginView.as_view(), name="login"),
    path('register/', views.register, name="register"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('update_profile/', views.update_profile, name="update_profile"),
    path('profile/', views.profile, name="profile")

]
