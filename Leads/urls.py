from django.urls import path
from . import views

# from .views import (lead_List, lead_detail, lead_create,  lead_update, lead_delete)

# app_name = "leads"

urlpatterns = [
    path("", views.LeadListView.as_view(), name = "leads"),
    path("<int:pk>/", views.LeadDetailView.as_view(), name = "lead_detail"),
    path("<int:pk>/update", views.LeadUpdateView.as_view(), name = "lead_update"),
    path("<int:pk>/delete", views.LeadDeleteView.as_view(), name = "lead_delete"),
    path("create/", views.LeadCreateView.as_view(), name = "lead_create"),
    
]