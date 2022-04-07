from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255, primary_key=True, unique=True)

    def __str__(self) -> str:
        return self.name

def due_date_validator(value):
    if value > timezone.now():
        return value
    raise ValidationError("due date bayad az alan bishtar bashad")


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    due_date = models.DateTimeField(null=True, validators=[due_date_validator])
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username}-{self.title}"