from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, Category, Supplier, InventoryHistory
from .forms import ProductForm, CategoryForm, SupplierForm, InventoryHistoryForm


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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:product_list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:product_list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('products:product_list')


class CategoryListView(ListView):
    model = Category
    template_name = 'products/category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'products/category_form.html'
    success_url = reverse_lazy('products:category_list')


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'products/category_form.html'
    success_url = reverse_lazy('products:category_list')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'products/category_confirm_delete.html'
    success_url = reverse_lazy('products:category_list')


class SupplierListView(ListView):
    model = Supplier
    template_name = 'products/supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 20


class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'products/supplier_form.html'
    success_url = reverse_lazy('products:supplier_list')


class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'products/supplier_form.html'
    success_url = reverse_lazy('products:supplier_list')


class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = Supplier
    template_name = 'products/supplier_confirm_delete.html'
    success_url = reverse_lazy('products:supplier_list')


class LowStockProductsView(ListView):
    model = Product
    template_name = 'products/low_stock_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(quantity_in_stock__lte=models.F('reorder_level'), is_active=True)


class InventoryHistoryListView(ListView):
    model = InventoryHistory
    template_name = 'products/inventory_history_list.html'
    context_object_name = 'history'
    paginate_by = 20
    ordering = ['-timestamp']


class InventoryHistoryCreateView(LoginRequiredMixin, CreateView):
    model = InventoryHistory
    form_class = InventoryHistoryForm
    template_name = 'products/inventory_history_form.html'
    success_url = reverse_lazy('products:inventory_history_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        product = form.instance.product
        if form.instance.transaction_type == 'IN':
            product.quantity_in_stock += form.instance.quantity
        elif form.instance.transaction_type == 'OUT':
            product.quantity_in_stock -= form.instance.quantity
        elif form.instance.transaction_type == 'ADJUSTMENT':
            product.quantity_in_stock = form.instance.quantity
        product.save()
        return response
