from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Leads, Agent
from .forms.lead_forms import LeadForm, LeadModelForm

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


def lead_create(request):
    form =LeadModelForm()
    if (request.method == "POST"):
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
            
    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)


def lead_update(request, pk):
    lead = lead.object.get(id=pk)
    context = {
        "lead": lead
        
    }
    return render(request, "leads/lead_update.html", context)

# def lead_create(request):
#     form =LeadModelForm()
#     if (request.method == "POST"):
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             print("form is valid")
#             print(form.cleaned_data)
#             first_name = form.cleaned_data["first_name"]
#             last_name = form.cleaned_data["last_name"]
#             age = form.cleaned_data["age"]
#             agent = Agent.objects.first()
#             Leads.objects.create(
#                 first_name = first_name, 
#                 last_name = last_name, 
#                 age = age, 
#                 agent = agent
#             )
#             print("leads has been created")
#             return redirect("/leads")
            
#     context = {
#         "form": form
#     }
#     return render(request, "leads/lead_create.html", context)
