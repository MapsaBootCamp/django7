from uuid import uuid4
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Wallet(models.Model):
    shomare_hesab = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.PositiveIntegerField()


    def save(self, *args, **kwargs) -> None:
        while Wallet.objects.filter(shomare_hesab=self.shomare_hesab).exists():
            self.shomare_hesab = uuid4()

        return super().save(*args, **kwargs)
