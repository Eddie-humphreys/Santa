from django.urls import path

from . import views

app_name = "presents"

urlpatterns = [
    path('', views.person_list, name='list'),
    path('<int:pk>/', views.idea_detail, name='idea_detail'),

]
