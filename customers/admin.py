from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'customer_type', 'is_active']
    list_filter = ['customer_type', 'is_active', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    readonly_fields = ['created_at', 'updated_at', 'total_orders']
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('Company Information', {
            'fields': ('company_name', 'customer_type', 'tax_id')
        }),
        ('Address', {
            'fields': ('billing_address', 'shipping_address', 'city', 'state', 'zip_code', 'country')
        }),
        ('Credit & Status', {
            'fields': ('credit_limit', 'is_active')
        }),
        ('Statistics', {
            'fields': ('total_orders',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
