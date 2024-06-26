from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Leads, Agent
from .forms.lead_forms import LeadForm, LeadModelForm

# Create your views here.
def landing_page(request):
    return render(request, "Layout/landing_page.html")

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
    lead = Leads.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if (request.method == "POST"):
         form = LeadModelForm(request.POST, instance=lead)
         if form.is_valid():
            form.save()
            return redirect("/leads")
            
    context = {
        "lead": lead,
        "form": form
    }
    return render(request, "leads/lead_update.html", context)

def lead_delete(request, pk):
    lead = Leads.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")
   


# def lead_update(request, pk):
#     lead = Leads.objects.get(id=pk)
#     form =LeadForm()
#     if (request.method == "POST"):
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             first_name = form.cleaned_data["first_name"]
#             last_name = form.cleaned_data["last_name"]
#             age = form.cleaned_data["age"]
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()
#             return redirect("/leads")
            
#     context = {
#         "form": form,
#         "lead": lead    
#     }
#     return render(request, "leads/lead_update.html", context)


# def lead_delete(request, pk):
#     return render(request, )

# def lead_create(request):
    # form =LeadModelForm()
    # if (request.method == "POST"):
    #     form = LeadModelForm(request.POST)
    #     if form.is_valid():
    #         print("form is valid")
    #         print(form.cleaned_data)
    #         first_name = form.cleaned_data["first_name"]
    #         last_name = form.cleaned_data["last_name"]
    #         age = form.cleaned_data["age"]
    #         agent = Agent.objects.first()
    #         Leads.objects.create(
    #             first_name = first_name, 
    #             last_name = last_name, 
    #             age = age, 
    #             agent = agent
    #         )
    #         print("leads has been created")
    #         return redirect("/leads")
            
    # context = {
    #     "form": form
    # }
#     return render(request, "leads/lead_create.html", context)
