from django.urls import path
from . import views
from .views import (
    PolicyListView,
    PolicyCreateView,
    PolicyDeleteView,
)

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    #path('policies', views.policies, name='policies'),
    path('view_policies', views.view_policies, name='view_policies'),
   # path('new_policy', views.new_policy, name='new_policy'),
    path('violations', views.violations, name='violations'),
    path('scan', views.scan, name='scan'),
    path('new_policy', PolicyCreateView.as_view(), name='new_policy'),
    path('policies', PolicyListView.as_view(), name='policies'),
    path('policies/<int:pk>/delete/', PolicyDeleteView.as_view(), name='delete_policy'),

]
