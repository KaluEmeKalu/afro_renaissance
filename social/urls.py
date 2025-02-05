from django.urls import path
from . import views

app_name = 'social'

urlpatterns = [
    path('', views.feed, name='feed'),
    path('explore/', views.explore, name='explore'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('messages/', views.messages, name='messages'),
    path('notifications/', views.notifications, name='notifications'),
]