"""
URL configuration for crmSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Leads.views import landing_page, LandingPageView, SignUpView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", LandingPageView.as_view(), name="landing_page"),
    path("leads/", include("Leads.urls")),
    path("agents/", include("Agents.urls")),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("reset-password/", PasswordResetView.as_view(), name="reset-password"),
    path(
        'password-reset-done/',
        PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'password-reset-complete/',
        PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),
    path("__reload__/", include("django_browser_reload.urls")),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#  namespace="leads"
