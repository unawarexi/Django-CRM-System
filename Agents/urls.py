from django.urls import path
from . import views

# from .views import (
#     AgentListView, AgentCreateView, AgentDetailView,
#     AgentUpdateView, AgentDeleteView
# )

app_name = 'agents'

urlpatterns = [
    path('', views.AgentListView.as_view(), name='agent-list'),
    path('<int:pk>/', views.AgentDetailView.as_view(), name='agent-detail'),
    path('<int:pk>/update/', views.AgentUpdateView.as_view(), name='agent-update'),
    path('<int:pk>/delete/', views.AgentDeleteView.as_view(), name='agent-delete'),
    path('create/', views.AgentCreateView.as_view(), name='agent-create'),
]
