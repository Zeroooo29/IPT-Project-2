from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    fields = ['product', 'quantity', 'unit_price', 'subtotal']
    readonly_fields = ['created_at']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'customer', 'status', 'final_total', 'created_at']
    list_filter = ['status', 'created_at', 'customer']
    search_fields = ['order_number', 'customer__first_name', 'customer__last_name']
    readonly_fields = ['created_at', 'updated_at', 'final_total']
    inlines = [OrderItemInline]
    fieldsets = (
        ('Order Information', {
            'fields': ('order_number', 'customer', 'status')
        }),
        ('Amounts', {
            'fields': ('total_amount', 'tax', 'shipping_cost', 'discount', 'final_total')
        }),
        ('Shipping & Notes', {
            'fields': ('shipping_address', 'notes')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at', 'shipped_date', 'delivered_date')
        }),
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'unit_price', 'subtotal']
    list_filter = ['order__created_at', 'product']
    search_fields = ['order__order_number', 'product__name']
    readonly_fields = ['created_at']
