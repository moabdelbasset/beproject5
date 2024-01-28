from django.db import models
from profiles.models import Profile  

class Task(models.Model):
    # Choices for status
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('inprogress', 'In Progress'),
        ('done', 'Done'),
        ('not_done', 'Not Done'),
    ]

    # Choices for priority
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

    # Fields
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='tasks')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'

