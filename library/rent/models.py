import datetime

from django.utils import timezone
from django.db import models

from user.models import Profile
from book.models import Book


class RentBook(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.RESTRICT)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
    rental_date = models.DateField(auto_now_add=True)
    return_bayad_date = models.DateField()
    return_avorde_date = models.DateField(null=True)

    def save(self, *args, **kwargs): 
        if self.return_bayad_date is None:
            self.return_bayad_date = timezone.now().date() + datetime.timedelta(days=20)
        return super().save(*args, **kwargs)
    def __str__(self) -> str:
        return f"{self.user.username} - {self.book.title}"