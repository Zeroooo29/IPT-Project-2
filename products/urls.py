from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # Products
    path('', views.ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    
    # Categories
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    
    # Suppliers
    path('suppliers/', views.SupplierListView.as_view(), name='supplier_list'),
    path('supplier/create/', views.SupplierCreateView.as_view(), name='supplier_create'),
    path('supplier/<int:pk>/edit/', views.SupplierUpdateView.as_view(), name='supplier_edit'),
    path('supplier/<int:pk>/delete/', views.SupplierDeleteView.as_view(), name='supplier_delete'),
    
    # Inventory
    path('low-stock/', views.LowStockProductsView.as_view(), name='low_stock_products'),
    path('inventory-history/', views.InventoryHistoryListView.as_view(), name='inventory_history_list'),
    path('inventory-history/create/', views.InventoryHistoryCreateView.as_view(), name='inventory_history_create'),
]
