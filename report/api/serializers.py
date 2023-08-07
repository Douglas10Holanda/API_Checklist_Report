from rest_framework import serializers
from report import models

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Report
        fields = '__all__'