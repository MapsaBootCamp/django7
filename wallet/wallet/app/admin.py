from django.contrib import admin

from .models import Wallet

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    pass