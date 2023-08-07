from django.db import models
from checklist.models import Checklist

class Report(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    state = models.BooleanField()
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE, related_name='reports')

    def __str__(self):
        return self.title