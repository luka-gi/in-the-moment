from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('',
         TemplateView.as_view(
             template_name="userAnalysis/userAnalysis.html"),
         name="userAnalysis"),
    path('james',
         TemplateView.as_view(
             template_name="userAnalysis/james.html"),
         name="james"),
    path('landon',
         TemplateView.as_view(
             template_name="userAnalysis/landon.html"),
         name="landon"),
    path('larry',
         TemplateView.as_view(
             template_name="userAnalysis/larry.html"),
         name="larry"),
    path('hannah',
         TemplateView.as_view(
             template_name="userAnalysis/hannah.html"),
         name="hannah"),
]
