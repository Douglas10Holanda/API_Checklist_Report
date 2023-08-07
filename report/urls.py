from django.urls import path
from .views import ReportDetail

urlpatterns = [
    path('<int:checklist_id>/', ReportDetail.as_view(), name="report")
]