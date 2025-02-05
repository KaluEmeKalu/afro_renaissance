from django.urls import path
from . import views

app_name = 'manifesto'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.section_detail, name='section_detail'),
]