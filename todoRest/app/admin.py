from django.contrib import admin
from django import forms
from app.models import Category, PostInstagrami, Todo

class PostForm(forms.ModelForm):
    class Meta:
        model = PostInstagrami
        fields = ["caption", "img"]

        
@admin.register(PostInstagrami)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "caption", "user")
    form = PostForm
    list_filter = ("user",)
    search_fields = ['caption', 'user__username']
    
    def save_model(self, request, obj, form, change):
        print("change", change)
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        return super().get_queryset(request).filter(user=request.user)
    # fieldsets = (
    #     (None, {
    #         'fields': ('img',)
    #     }),
    #     ('اطلاعات اصلی', {
    #         'classes': ('collapse',),
    #         'fields': ('caption', 'user'),
    #     }),
    # )

admin.site.register(Todo)
admin.site.register(Category)
# admin.site.register(PostInstagrami, PostAdmin)