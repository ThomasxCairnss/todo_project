from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    # New fields:
    category = models.CharField(max_length=100, null=True, blank=True, help_text="E.g., Work, Personal, Errands")
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    
    def __str__(self):
        return self.title
