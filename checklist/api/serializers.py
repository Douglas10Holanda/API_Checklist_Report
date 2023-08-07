from rest_framework import serializers
from checklist import models

class ChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Checklist
        fields = "__all__"