from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('suppliers/', views.SupplierListView.as_view(), name='supplier_list'),
    path('low-stock/', views.LowStockProductsView.as_view(), name='low_stock_products'),
]
