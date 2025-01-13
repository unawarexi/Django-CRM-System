from django import forms
from Leads.models import Agent

class AgentModelForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ('user',)  # Field related to User, but also linked to the Agent model
