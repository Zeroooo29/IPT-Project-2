from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Order, OrderItem


class OrderListView(ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'
    paginate_by = 20

    def get_queryset(self):
        queryset = Order.objects.all()
        status = self.request.GET.get('status')
        customer = self.request.GET.get('customer')
        
        if status:
            queryset = queryset.filter(status=status)
        if customer:
            queryset = queryset.filter(customer__id=customer)
        
        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Order.STATUS_CHOICES
        return context


class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = self.object.items.all()
        return context


class CustomerOrdersView(ListView):
    model = Order
    template_name = 'orders/customer_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return Order.objects.filter(customer__id=customer_id).order_by('-created_at')
