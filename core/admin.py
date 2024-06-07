from django.contrib import admin
from .models import Phone, Recipient


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ("brand", "model", "imei", "status", "added_date")
    list_filter = ("brand", "status", "added_date")
    search_fields = ("brand", "model", "imei")
    ordering = ("-added_date",)
    readonly_fields = ("added_date",)
    fieldsets = (
        (None, {
            'fields': ('brand', 'model', 'imei', 'status')
        }),
        ('Əlavə məlumat', {
            'fields': ('note',),
            'classes': ('collapse',),
        }),
        ('Tarix', {
            'fields': ('added_date',),
        }),
    )


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    list_filter = ("name", "email")
    search_fields = ("name", "email")
