from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_year = models.DateField()

    class Meta:
        ordering = ['title']

    def __str__(self) -> str:
        return self.title