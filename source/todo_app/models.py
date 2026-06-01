from django.db import models

# Create your models here.

class TodoItem(models.Model):
    status_choices = [('new','новая'),('in_progress','в процессе'),('done','сделано')]

    description = models.TextField(max_length=400, null=False, blank=False, verbose_name="description")
    status = models.CharField(null=False, blank=False, verbose_name="status", choices=status_choices, max_length=30)
    date = models.DateField(null=True, blank=True, verbose_name="date")

    def __str__(self):
        return self.description

    class Meta:
        db_table = "task"
        verbose_name = "task"
