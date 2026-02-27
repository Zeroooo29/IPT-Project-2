from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import StaffMember
from .forms import StaffMemberForm


class StaffListView(ListView):
    model = StaffMember
    template_name = 'staff/staff_list.html'
    context_object_name = 'staff'
    paginate_by = 20

    def get_queryset(self):
        queryset = StaffMember.objects.all()
        department = self.request.GET.get('department')
        position = self.request.GET.get('position')
        active = self.request.GET.get('active')
        
        if department:
            queryset = queryset.filter(department=department)
        if position:
            queryset = queryset.filter(position=position)
        if active:
            queryset = queryset.filter(is_active=(active == 'true'))
        
        return queryset.order_by('department', 'position')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = StaffMember.DEPARTMENT_CHOICES
        context['positions'] = StaffMember.POSITION_CHOICES
        return context


class StaffDetailView(DetailView):
    model = StaffMember
    template_name = 'staff/staff_detail.html'
    context_object_name = 'staff_member'


class StaffCreateView(LoginRequiredMixin, CreateView):
    model = StaffMember
    form_class = StaffMemberForm
    template_name = 'staff/staff_form.html'
    success_url = reverse_lazy('staff:staff_list')


class StaffUpdateView(LoginRequiredMixin, UpdateView):
    model = StaffMember
    form_class = StaffMemberForm
    template_name = 'staff/staff_form.html'
    success_url = reverse_lazy('staff:staff_list')


class StaffDeleteView(LoginRequiredMixin, DeleteView):
    model = StaffMember
    template_name = 'staff/staff_confirm_delete.html'
    success_url = reverse_lazy('staff:staff_list')


class DepartmentStaffView(ListView):
    model = StaffMember
    template_name = 'staff/department_staff.html'
    context_object_name = 'staff'

    def get_queryset(self):
        department = self.kwargs['department']
        return StaffMember.objects.filter(department=department).order_by('position')
