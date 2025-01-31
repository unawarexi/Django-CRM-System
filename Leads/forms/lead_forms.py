from django import forms
from .. import models
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = models.Leads
        fields = (
            "first_name",
            "last_name",
            "age",
            "agent",
        )


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}


class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Leads
        fields = ('category',)


class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=models.Agent.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        agents = models.Agent.objects.filter(organisation=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset = agents
