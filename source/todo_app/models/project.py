from django.db import models

class Project(models.Model):
    begining_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)
    project_title = models.CharField(max_length=200, null=False, blank=False)
    project_description = models.TextField(max_length=500, null=False, blank=False)
