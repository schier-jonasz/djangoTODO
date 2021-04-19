from django.db import models

# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length = 200)
    createDate = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default = False)

    def __str__(self):
        return self.taskTitle

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
