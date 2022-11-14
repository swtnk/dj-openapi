"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.urls import path, include
from openapi.views import SpecificationLists, LoginView, LogoutView

admin.site.site_header = settings.APP_NAME
admin.site.site_title = settings.APP_NAME
admin.site.index_title = settings.APP_NAME

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("openapi/", include("openapi.urls")),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", login_required(LogoutView.as_view()), name="logout"),
    path("", login_required(SpecificationLists.as_view()), name="dashboard"),
]
