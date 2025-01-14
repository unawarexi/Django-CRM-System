from django.contrib import admin
from .models import User, Leads, Agent, UserProfile, Category

# Register your models here.

admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(User)
admin.site.register(Leads)
admin.site.register(Agent)
