from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=20)
    description = models.TextField(default="No Description")
    PRIORITY_OPTIONS = (
        ("H","High"),
        ("M","Medium"),
        ("L","Low")
    )
    priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS, default="L")
    done = models.BooleanField()
    updateDate = models.DateTimeField(auto_now=True)
    createDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task}"
