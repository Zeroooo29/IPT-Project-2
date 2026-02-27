from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, OrderItem
from .forms import OrderForm, OrderItemForm


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


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order_form.html'
    success_url = reverse_lazy('orders:order_list')


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order_form.html'
    success_url = reverse_lazy('orders:order_list')


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = 'orders/order_confirm_delete.html'
    success_url = reverse_lazy('orders:order_list')


class OrderItemCreateView(LoginRequiredMixin, CreateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'orders/orderitem_form.html'

    def get_success_url(self):
        return reverse_lazy('orders:order_detail', kwargs={'pk': self.object.order.pk})

    def get_initial(self):
        initial = super().get_initial()
        order_id = self.kwargs.get('order_id')
        if order_id:
            initial['order'] = order_id
        return initial


class OrderItemUpdateView(LoginRequiredMixin, UpdateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'orders/orderitem_form.html'

    def get_success_url(self):
        return reverse_lazy('orders:order_detail', kwargs={'pk': self.object.order.pk})


class OrderItemDeleteView(LoginRequiredMixin, DeleteView):
    model = OrderItem
    template_name = 'orders/orderitem_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('orders:order_detail', kwargs={'pk': self.object.order.pk})


class CustomerOrdersView(ListView):
    model = Order
    template_name = 'orders/customer_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return Order.objects.filter(customer__id=customer_id).order_by('-created_at')
