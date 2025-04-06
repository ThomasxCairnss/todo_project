from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/new/', views.task_create, name='task_create'),
    path('task/edit/<int:pk>/', views.task_update, name='task_update'),
    path('task/delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('export/csv/', views.export_tasks_csv, name='export_tasks_csv'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('summary/', views.summary_view, name='summary'),
    path('calendar/', views.calendar_view, name='calendar'),
]
