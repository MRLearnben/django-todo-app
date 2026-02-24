from django.db import models

# Create your models here.

class ToDo(models.Model):
    title = models.CharField(max_length=200)  # Required title, up to 200 characters
    description = models.TextField(blank=True, null=True)  # Optional description
    completed = models.BooleanField(default=False)  # Completed status, starts as False
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created

    def __str__(self):
        return self.title  # Shows title in admin panel