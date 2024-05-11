from django.contrib import admin
from .models import User, Leads, Agent
# Register your models here.

admin.site.register(User)
admin.site.register(Leads)
admin.site.register(Agent)