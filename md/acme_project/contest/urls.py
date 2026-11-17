from django.urls import path
from . import views

app_name = 'contest'

urlpatterns = [
    path('', views.proposal_create, name='create'),
    path('list/', views.contest_list, name='list'),
    path('<int:pk>/edit/', views.proposal_create, name='edit'),
    path('<int:pk>/delete/', views.proposal_create, name='delete'),
]