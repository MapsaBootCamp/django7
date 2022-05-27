from django.db import models
from django.conf import settings

from rest_framework.authtoken.models import Token

from .signals import post_done_todo


class AuditModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Category(AuditModel):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'user'], name='unique category')
        ]


class Todo(AuditModel):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    due_date = models.DateField()
    done = models.BooleanField(default=False)

    def todo_done(self):
        self.done = True
        self.save()
        post_done_todo.send(sender=self.__class__, user=self.category.user)


    def __str__(self):
        return self.title