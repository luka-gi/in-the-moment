"""django_project URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/

Examples
--------
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
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',
         TemplateView.as_view(template_name="home.html"),
         name="home"),
    path('team',
         TemplateView.as_view(template_name="team.html"),
         name="team"),
    path('about',
         TemplateView.as_view(template_name="about.html"),
         name="about"),
    path('map',
         TemplateView.as_view(template_name="map.html"),
         name="map"),
    path('userAnalysis',
         TemplateView.as_view(template_name="userAnalysis.html"),
         name="userAnalysis"),
    path('james',
         TemplateView.as_view(template_name="james.html"),
         name="james"),
    path('sam',
         TemplateView.as_view(template_name="sam.html"),
         name="sam"),
    path('larry',
         TemplateView.as_view(template_name="larry.html"),
         name="larry"),
    path('hannah',
         TemplateView.as_view(template_name="hannah.html"),
         name="hannah"),
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += staticfiles_urlpatterns()
