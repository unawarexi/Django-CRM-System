from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    path("", views.lead_List, name = "leads"),
    path("<pk>/", views.lead_detail, name = "leadDetail"),
    
]