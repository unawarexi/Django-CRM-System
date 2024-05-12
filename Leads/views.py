from django.http import HttpResponse
from django.shortcuts import render
from .models import Leads

# Create your views here.
def lead_List(request):
    leads = Leads.objects.all()
    context = {
        "leads": leads
    }
    return render (request, "leads/leads_list.html", context)



def lead_detail(request, pk):
    
    lead = Leads.objects.get(id=pk)
    context = {
        "lead" : lead
    }
    return render(request, "leads/lead_detail.html", context)
