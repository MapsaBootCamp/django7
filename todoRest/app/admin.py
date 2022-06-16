from django.contrib import admin
from django import forms
from app.models import Category, FollowerTable, FollowerUser, PostInstagramiProxyAdmin, Todo

class PostForm(forms.ModelForm):
    class Meta:
        model = PostInstagramiProxyAdmin
        fields = ["caption", "img"]

        
@admin.register(PostInstagramiProxyAdmin)
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
        if request.user.is_superuser:
            return super().get_queryset(request)
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
admin.site.register(FollowerTable)
admin.site.register(FollowerUser)
# admin.site.register(PostInstagramiProxyAdmin, PostAdmin)