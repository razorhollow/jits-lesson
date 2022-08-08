from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('techniques/', views.technique_index, name='technique_index'),
  path('techniques/<int:technique_id>/', views.technique_detail, name='technique_detail'),
]