from django.urls import path
from .views import *

urlpatterns = [
    path("", LandingPageView.as_view(), name="landing_page"),
    path("dashboard/", DashboardView.as_view(), name="dashboard")
]
