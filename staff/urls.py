from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('', views.StaffListView.as_view(), name='staff_list'),
    path('member/<int:pk>/', views.StaffDetailView.as_view(), name='staff_detail'),
    path('department/<str:department>/', views.DepartmentStaffView.as_view(), name='department_staff'),
]
