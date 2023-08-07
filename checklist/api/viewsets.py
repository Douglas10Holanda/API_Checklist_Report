from rest_framework import viewsets
from checklist.api import serializers
from checklist import models

class ChecklistViewsets(viewsets.ModelViewSet):
    serializer_class = serializers.ChecklistSerializer
    queryset = models.Checklist.objects.all()