from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('', views.StaffListView.as_view(), name='staff_list'),
    path('member/<int:pk>/', views.StaffDetailView.as_view(), name='staff_detail'),
    path('member/create/', views.StaffCreateView.as_view(), name='staff_create'),
    path('member/<int:pk>/edit/', views.StaffUpdateView.as_view(), name='staff_edit'),
    path('member/<int:pk>/delete/', views.StaffDeleteView.as_view(), name='staff_delete'),
    path('department/<str:department>/', views.DepartmentStaffView.as_view(), name='department_staff'),
]
