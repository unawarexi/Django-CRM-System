from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Leads, Agent, Category
from .forms.lead_forms import (
    LeadForm,
    LeadModelForm,
    CustomUserCreationForm,
    AssignAgentForm,
    LeadCategoryUpdateForm,
)
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from Agents.mixins import OrganisorAndLoginRequiredMixin

# import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


class SignUpView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class LandingPageView(generic.TemplateView):
    template_name = "Layout/landing_page.html"


class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/leads_list.html"
    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Leads.objects.filter(
                organisation=user.userprofile, agent__isnull=False
            )
        else:
            queryset = Leads.objects.filter(
                organisation=user.agent.organisation, agent__isnull=False
            )

            # filter for the agent that is logged in
            queryset = queryset.filter(agent__user=user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organisor:
            queryset = Leads.objects.filter(
                organisation=user.userprofile, agent__isnull=True
            )
            context.update({"unassigned_leads": queryset})
        return context


class LeadDetailView(generic.DetailView):
    template_name = "leads/lead_detail.html"
    context_object_name = "lead"

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Leads.objects.filter(organisation=user.userprofile)
        else:
            queryset = Leads.objects.filter(organisation=user.agent.organisation)

            # filter for the agent that is logged in
            queryset = queryset.filter(agent__user=user)
        return queryset


class LeadCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads")

    def form_valid(self, form):
        # TODO send email
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see a new lead",
            from_email="test@test.com",
            recipient_list=["unawarexi@gmail.com"],
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm

    def get_queryset(self):
        user = self.request.user

        return Leads.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        return reverse("leads")


class LeadDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    template_name = "leads/lead_delete.html"

    def get_queryset(self):
        user = self.request.user

        return Leads.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        return reverse("leads")


class AssignAgentView(OrganisorAndLoginRequiredMixin, generic.FormView):
    template_name = "leads/assign_agents.html"
    form_class = AssignAgentForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignAgentView, self).get_form_kwargs(**kwargs)
        kwargs.update({"request": self.request})
        return kwargs

    def get_success_url(self):
        return reverse("leads")

    def form_valid(self, form):
        agent = form.cleaned_data["agent"]
        lead = Leads.objects.get(id=self.kwargs["pk"])
        lead.agent = agent
        lead.save()
        return super(AssignAgentView, self).form_valid(form)


class CategoryListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/category_list.html"
    context_object_name = "category_list"

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        user = self.request.user

        if user.is_organisor:
            queryset = Leads.objects.filter(organisation=user.userprofile)
        else:
            queryset = Leads.objects.filter(organisation=user.agent.organisation)

        context.update(
            {"unassigned_lead_count": queryset.filter(category__isnull=True).count()}
        )
        return context

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        if user.is_organisor:
            queryset = Category.objects.filter(organisation=user.userprofile)
        else:
            queryset = Category.objects.filter(organisation=user.agent.organisation)
        return queryset


class CategoryDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/category_detail.html"
    context_object_name = "category"

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        if user.is_organisor:
            queryset = Category.objects.filter(organisation=user.userprofile)
        else:
            queryset = Category.objects.filter(organisation=user.agent.organisation)
        return queryset


class LeadCategoryUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "leads/lead_category_update.html"
    form_class = LeadCategoryUpdateForm

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        if user.is_organisor:
            queryset = Leads.objects.filter(organisation=user.userprofile)
        else:
            queryset = Leads.objects.filter(organisation=user.agent.organisation)
            # filter for the agent that is logged in
            queryset = queryset.filter(agent__user=user)
        return queryset

    def get_success_url(self):
        return reverse("lead_detail", kwargs={"pk": self.get_object().id})

    def form_valid(self, form):
        lead_before_update = self.get_object()
        instance = form.save(commit=False)
        converted_category = Category.objects.get(name="Converted")
        if form.cleaned_data["category"] == converted_category:
            # update the date at which this lead was converted
            if lead_before_update.category != converted_category:
                # this lead has now been converted
                instance.converted_date = datetime.datetime.now()
        instance.save()
        return super(LeadCategoryUpdateView, self).form_valid(form)





# Create your views here.
def landing_page(request):
    return render(request, "Layout/landing_page.html")


def lead_List(request):
    leads = Leads.objects.all()
    context = {"leads": leads}
    return render(request, "leads/leads_list.html", context)


def lead_detail(request, pk):

    lead = Leads.objects.get(id=pk)
    context = {"lead": lead}
    return render(request, "leads/lead_detail.html", context)


def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")

    context = {"form": form}
    return render(request, "leads/lead_create.html", context)


def lead_update(request, pk):
    lead = Leads.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")

    context = {"lead": lead, "form": form}
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
