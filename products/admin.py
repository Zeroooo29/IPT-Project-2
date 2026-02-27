from django.contrib import admin
from .models import Category, Supplier, Product, InventoryHistory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_person', 'email', 'phone', 'city']
    search_fields = ['name', 'contact_person', 'email']
    list_filter = ['city', 'state']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'contact_person', 'email', 'phone')
        }),
        ('Address', {
            'fields': ('address', 'city', 'state', 'zip_code')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'sku', 'category', 'price', 'quantity_in_stock', 'is_active']
    list_filter = ['category', 'supplier', 'is_active']
    search_fields = ['name', 'sku', 'description']
    readonly_fields = ['created_at', 'updated_at', 'profit_margin', 'needs_reorder']
    fieldsets = (
        ('Product Information', {
            'fields': ('name', 'sku', 'description', 'category', 'supplier')
        }),
        ('Pricing & Stock', {
            'fields': ('price', 'cost', 'quantity_in_stock', 'reorder_level', 'needs_reorder')
        }),
        ('Status & Metrics', {
            'fields': ('is_active', 'profit_margin')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(InventoryHistory)
class InventoryHistoryAdmin(admin.ModelAdmin):
    list_display = ['product', 'transaction_type', 'quantity', 'timestamp']
    list_filter = ['transaction_type', 'timestamp', 'product']
    search_fields = ['product__name', 'reason']
    readonly_fields = ['timestamp']
    fieldsets = (
        ('Transaction Information', {
            'fields': ('product', 'transaction_type', 'quantity', 'reason')
        }),
        ('Timestamp', {
            'fields': ('timestamp',),
            'classes': ('collapse',)
        }),
    )
