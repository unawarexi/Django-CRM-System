from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Leads, Agent
from .forms.lead_forms import LeadForm, LeadModelForm, CustomUserCreationForm
from django.views import generic
# import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


class SignUpView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    
    def get_success_url(self):
        return reverse("login")
    
    
# class LoginInView(LoginView):
#     template_name = "registration/login.html"
#     form_class = AuthenticationForm

#     def get_success_url(self):
#         return reverse("landing_page")
    
    
# # Logout view (you can customize the logout behavior if needed)
# class LoggingOutView(LoginRequiredMixin, LogoutView):
#     next_page = 'login'  # Redirect to login page after logout

#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return redirect(self.next_page)

class LandingPageView(generic.TemplateView):
    template_name = "Layout/landing_page.html"
    
class LeadListView(generic.ListView):
    template_name = "leads/leads_list.html"
    queryset = Leads.objects.all()
    context_object_name = "leads"
    
class LeadDetailView(generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Leads.objects.all()
    context_object_name = "lead"
    

class LeadCreateView(generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse("leads")
    
    def  form_valid(self, form):
        #TODO send email
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see a new lead",
            from_email="test@test.com",
            recipient_list=["unawarexi@gmail.com"]
        )
        return super(LeadCreateView, self).form_valid(form)
    
    
class LeadUpdateView(generic.UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Leads.objects.all()
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse("leads")
    
class LeadDeleteView(generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Leads.objects.all()
    
    def get_success_url(self):
        return reverse("leads")
    

    
    
    
     


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
