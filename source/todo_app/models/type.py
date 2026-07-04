from django.db import models

class Type(models.Model):
    type_title = models.TextField(max_length=200, null=False, blank=False, verbose_name="Заголовок типа")

    def __str__(self):
        return self.type_title