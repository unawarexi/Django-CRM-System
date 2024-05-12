from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    path("", views.lead_List, name = "leads"),
    path("<int:pk>/", views.lead_detail, name = "leadDetail"),
    path("<int:pk>/update", views.lead_update, name = "lead_update"),
    path("create/", views.lead_create, name = "leadCreate"),
    
]