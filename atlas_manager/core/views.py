from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class LandingPageView(TemplateView):
    template_name = "landing.html"

class DashboardView(TemplateView):
    template_name = "dashboard.html"