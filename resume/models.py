from django.db import models
from authentication.models import User

class Resume(models.Model):
    title = models.CharField(max_length=50, unique=True)
    template = models.CharField(max_length=100)
    personal = models.JSONField()
    education = models.JSONField()
    experience = models.JSONField()
    skills = models.JSONField()
    projects = models.JSONField()
    achivements = models.JSONField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('created_by', 'title')
