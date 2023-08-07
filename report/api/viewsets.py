from rest_framework import viewsets
from report.api import serializers
from report.models import Report

class ReportViewsets(viewsets.ModelViewSet):
    serializer_class = serializers.ReportSerializer
    queryset = Report.objects.all()

    def get(self, request, id):
        queryset = queryset.filter(checklist_id=id)
        return self.serializer_class.data