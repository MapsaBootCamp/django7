from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


User = get_user_model()


class Profile(User):
    LABEL = [
        ("Student", "student"),
        ("Professor", "professor"),
        ("Regular", "regular")
    ]
    address = models.TextField()
    phone_number = models.CharField(null=True, max_length=10, validators=[RegexValidator(r'^9\d{9}$')])
    img = models.ImageField(upload_to='profile/', null=True, blank=True)
    join_date = models.DateField(auto_now_add=True)
    membership_expire_date = models.DateField()
    LABEL = models.CharField(max_length=50, choices=LABEL)
    
    class Meta:
        verbose_name = "Profile"

