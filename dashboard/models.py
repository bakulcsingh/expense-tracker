from django.db import models
from django.contrib.auth.models import User

class SavedReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    report_type = models.CharField(max_length=20)  # e.g., 'category', 'monthly', 'comparison'
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} ({self.report_type})"