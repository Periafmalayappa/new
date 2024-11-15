from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.about, name='about'),
]