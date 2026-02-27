from django.db import models
from django.contrib.auth.models import User


class StaffMember(models.Model):
    POSITION_CHOICES = [
        ('MANAGER', 'Manager'),
        ('SALESPERSON', 'Salesperson'),
        ('WAREHOUSE', 'Warehouse Staff'),
        ('ACCOUNTANT', 'Accountant'),
        ('SUPERVISOR', 'Supervisor'),
    ]

    DEPARTMENT_CHOICES = [
        ('SALES', 'Sales'),
        ('WAREHOUSE', 'Warehouse'),
        ('ACCOUNTING', 'Accounting'),
        ('MANAGEMENT', 'Management'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=50, unique=True)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField()
    date_hired = models.DateField(auto_now_add=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.position}"

    class Meta:
        ordering = ['department', 'position']
