from django.contrib import admin

from app.models import Category, Todo

admin.site.register(Todo)
admin.site.register(Category)