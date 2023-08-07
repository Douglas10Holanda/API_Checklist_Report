"""
URL configuration for report_builder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from rest_framework import routers
from checklist.api import viewsets as checklistViewsets
from report.api import viewsets as reportViewsets

route = routers.DefaultRouter()

route.register(r'reports', reportViewsets.ReportViewsets, basename="reports")
route.register(r'checklists', checklistViewsets.ChecklistViewsets, basename="checklists")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Listreports/', include('report.urls')),
    path('', include(route.urls))
]