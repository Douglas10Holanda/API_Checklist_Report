from django.shortcuts import render
from rest_framework.views import APIView
from .models import Report
from .api.serializers import ReportSerializer
from rest_framework.response import Response

class ReportDetail(APIView):
    def get(self, request, checklist_id, format=None):
        reports = Report.objects.filter(checklist_id=checklist_id)#.values("title","description","state", "checklist__title")
        serializer = ReportSerializer(reports, many=True)
        # result = []
        # for report in reports:
        #    result.append({
        #        "title": report["title"],
        #        "description": report["description"],
        #        "state": report["state"],
        #        "checklist": report["checklist"]
        #    })
        return Response(serializer.data)