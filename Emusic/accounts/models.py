from django.db import models
from django.contrib.auth.models import User

# Subscription Plan Model
class SubscriptionPlan(models.Model):
    PLAN_CHOICES = [
        ('FREE', 'Free'),
        ('PREMIUM', 'Premium'),
        ('FAMILY', 'Family'),
    ]
    name = models.CharField(max_length=50, choices=PLAN_CHOICES, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    description = models.TextField()
    users = models.ManyToManyField(User, related_name='subscription_plans', blank=True)

    def __str__(self):
        return self.name

# Song Category Model
class SongCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Genre Model
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(SongCategory, on_delete=models.CASCADE, related_name='genres')

    def __str__(self):
        return f"{self.name} ({self.category.name})"

# Notification Model
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}"
