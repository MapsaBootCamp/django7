from unicodedata import category
from django.db import models
from django.utils.text import slugify

from user.models import Profile


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class BookManager(models.Manager):
    def ketabaye_adabi(self):
        return self.filter(category__name="ادبی")


class Book(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    author1 = models.CharField(max_length=255)
    author2 = models.CharField(max_length=255, null=True, blank=True)
    author3 = models.CharField(max_length=255, null=True, blank=True)
    author4 = models.CharField(max_length=255, null=True, blank=True)
    translated = models.BooleanField()
    translator1 = models.CharField(max_length=255, null=True, blank=True)
    translator2 = models.CharField(max_length=255, null=True, blank=True)
    translator3 = models.CharField(max_length=255, null=True, blank=True)
    translator4 = models.CharField(max_length=255, null=True, blank=True)
    publisher = models.CharField(max_length=255)
    qty = models.SmallIntegerField()
    available_qty = models.SmallIntegerField(null=True, blank=True)
    objects = models.Manager()
    mandaravordi_manager = BookManager()
    slug = models.SlugField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title, allow_unicode=True)
        if self.available_qty is None:
            self.available_qty = self.qty
        if self.available_qty > self.qty:
            raise Exception("available_qty can not be greater than qty")
        return super().save(*args, **kwargs)

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rate = models.SmallIntegerField(default=3)
