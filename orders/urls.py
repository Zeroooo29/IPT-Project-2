from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    # Orders
    path('', views.OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('order/create/', views.OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/edit/', views.OrderUpdateView.as_view(), name='order_edit'),
    path('order/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order_delete'),
    
    # Order Items
    path('order/<int:order_id>/item/create/', views.OrderItemCreateView.as_view(), name='orderitem_create'),
    path('orderitem/<int:pk>/edit/', views.OrderItemUpdateView.as_view(), name='orderitem_edit'),
    path('orderitem/<int:pk>/delete/', views.OrderItemDeleteView.as_view(), name='orderitem_delete'),
    
    # Customer Orders
    path('customer/<int:customer_id>/', views.CustomerOrdersView.as_view(), name='customer_orders'),
]
