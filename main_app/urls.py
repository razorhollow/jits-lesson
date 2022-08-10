from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('techniques/', views.technique_index, name='technique_index'),
  path('techniques/<int:technique_id>/', views.technique_detail, name='technique_detail'),
  path('techniques/create/', views.TechniqueCreate.as_view(), name='technique_create'),
  path('techniques/<int:pk>/update/', views.TechniqueUpdate.as_view(), name='technique_update'),
  path('techniques/<int:pk>/delete/', views.TechniqueDelete.as_view(), name='technique_delete'),
  path('accounts/signup/', views.signup, name='signup'),
  path('plan/', views.lesson_plan, name='lesson_plan'),
  path('plan/load', views.load_plan, name='load_plan')
]