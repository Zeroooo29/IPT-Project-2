from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Customer


class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = 'customers'
    paginate_by = 20

    def get_queryset(self):
        queryset = Customer.objects.all()
        customer_type = self.request.GET.get('type')
        search = self.request.GET.get('search')
        active = self.request.GET.get('active')
        
        if customer_type:
            queryset = queryset.filter(customer_type=customer_type)
        if search:
            queryset = queryset.filter(
                Q(first_name__icontains=search) | Q(last_name__icontains=search) | Q(email__icontains=search)
            )
        if active:
            queryset = queryset.filter(is_active=(active == 'true'))
        
        return queryset.order_by('first_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer_types'] = Customer.CUSTOMER_TYPES
        return context


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/customer_detail.html'
    context_object_name = 'customer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = self.object.orders.all()[:10]
        return context
