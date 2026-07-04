from django.db import models
# Create your models here.

class TodoItem(models.Model):
    title = models.TextField(max_length=200, null=False, blank=False, verbose_name="Заголовок")
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name="Описание")
    status = models.ForeignKey('todo_app.Status', related_name="task", on_delete=models.CASCADE, null=False, blank=False, verbose_name="Статус")
    type = models.ForeignKey('todo_app.Type', related_name="task", on_delete=models.CASCADE, null=False, blank=False, verbose_name="Тип")
    date_of_add = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    date_of_update = models.DateField(auto_now=True, verbose_name="Последние изменения")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Task"
        verbose_name = "task"
