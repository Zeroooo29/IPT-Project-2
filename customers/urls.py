from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('', views.CustomerListView.as_view(), name='customer_list'),
    path('customer/<int:pk>/', views.CustomerDetailView.as_view(), name='customer_detail'),
]
