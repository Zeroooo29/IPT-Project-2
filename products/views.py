from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db import models
from .models import Product, Category, Supplier, InventoryHistory


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 20

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.GET.get('category')
        search = self.request.GET.get('search')
        
        if category:
            queryset = queryset.filter(category__id=category)
        if search:
            queryset = queryset.filter(name__icontains=search)
        
        return queryset.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inventory_history'] = self.object.inventory_history.all()[:10]
        return context


class CategoryListView(ListView):
    model = Category
    template_name = 'products/category_list.html'
    context_object_name = 'categories'


class SupplierListView(ListView):
    model = Supplier
    template_name = 'products/supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 20


class LowStockProductsView(ListView):
    model = Product
    template_name = 'products/low_stock_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(quantity_in_stock__lte=models.F('reorder_level'), is_active=True)
