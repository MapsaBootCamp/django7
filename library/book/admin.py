from django.contrib import admin

from .models import Book, Category, Comment

class CommentInline(admin.StackedInline):
    model = Comment

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

# admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(Comment)