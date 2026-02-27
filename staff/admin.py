from django.contrib import admin
from .models import StaffMember


@admin.register(StaffMember)
class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'employee_id', 'position', 'department', 'is_active']
    list_filter = ['department', 'position', 'is_active', 'date_hired']
    search_fields = ['user__first_name', 'user__last_name', 'employee_id', 'phone']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('User Account', {
            'fields': ('user', 'employee_id')
        }),
        ('Position & Department', {
            'fields': ('position', 'department', 'salary')
        }),
        ('Personal Information', {
            'fields': ('phone', 'address', 'date_of_birth')
        }),
        ('Employment', {
            'fields': ('date_hired', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
