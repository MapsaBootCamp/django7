from django.contrib import admin

from app.models import Category, PostInstagrami, Todo


@admin.register(PostInstagrami)
class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Todo)
admin.site.register(Category)