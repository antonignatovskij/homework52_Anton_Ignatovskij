from django.db import models

class Status(models.Model):
    status_title = models.TextField(max_length=200, null=False, blank=False, verbose_name="Заголовок статуса")

    def __str__(self):
        return self.status_title