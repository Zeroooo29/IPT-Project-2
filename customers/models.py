from django.db import models


class Customer(models.Model):
    CUSTOMER_TYPES = [
        ('RETAIL', 'Retail'),
        ('WHOLESALE', 'Wholesale'),
        ('CORPORATE', 'Corporate'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    customer_type = models.CharField(max_length=20, choices=CUSTOMER_TYPES, default='RETAIL')
    billing_address = models.TextField()
    shipping_address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100, default='USA')
    company_name = models.CharField(max_length=200, blank=True, null=True)
    tax_id = models.CharField(max_length=50, blank=True, null=True)
    credit_limit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def total_orders(self):
        return self.orders.count()

    class Meta:
        ordering = ['first_name', 'last_name']
