from django.db import models
from django.contrib.auth.models import User

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
    category = models.CharField(
        max_length=100, 
        null=True, 
        blank=True, 
        help_text="E.g., Work, Personal, Errands"
    )
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    # Optional: track if points have been awarded for this task to avoid duplicate awards
    points_awarded = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weekly_points = models.IntegerField(default=0)
    overall_points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def add_points(self, points=100):
        """
        Add points to both weekly and overall totals.
        """
        self.weekly_points += points
        self.overall_points += points
        self.save()

    def reset_weekly_points(self):
        """
        Resets the weekly points to 0. Useful if you later want to clear the weekly total.
        """
        self.weekly_points = 0
        self.save()
