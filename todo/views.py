from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
import json
from .forms import TaskForm
import pandas as pd

def calendar_view(request):
    tasks = Task.objects.all()
    events = []
    for task in tasks:
        if task.due_date:  # only include tasks with a due date
            # Set the color based on the task's priority
            if task.priority.lower() == 'low':
                color = 'green'
            elif task.priority.lower() == 'medium':
                color = 'yellow'
            elif task.priority.lower() == 'high':
                color = 'red'
            else:
                color = None  # default if no priority is set
            
            events.append({
                'title': task.title,
                'start': task.due_date.strftime('%Y-%m-%d'),
                'color': color,
            })
    context = {
        'events_json': json.dumps(events)
    }
    return render(request, 'todo/calendar.html', context)

def task_list(request):
    # Retrieve all tasks and sort them by due_date (ascending)
    tasks = Task.objects.all().order_by('due_date')
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def summary_view(request):
    # Retrieve tasks data with due_date and status
    tasks = Task.objects.all().values('due_date', 'status')
    df = pd.DataFrame(list(tasks))
    
    # If data exists, compute pivot tables; otherwise, use empty values.
    if not df.empty:
        # Pivot table: Tasks by Due Date and Status
        pivot_by_day = df.pivot_table(
            index='due_date', 
            columns='status', 
            aggfunc='size', 
            fill_value=0
        )
        # Convert pivot table into a list of dictionaries (one per row)
        pivot_by_day_data = pivot_by_day.reset_index().to_dict(orient='records')
        # Get column headers (include the index column first)
        pivot_by_day_columns = ['due_date'] + list(pivot_by_day.columns)
        
        # Pivot table: Tasks by Status (simple count)
        pivot_by_status = df['status'].value_counts().to_dict()
    else:
        pivot_by_day_data = []
        pivot_by_day_columns = []
        pivot_by_status = {}

    context = {
        'pivot_by_day_data': pivot_by_day_data,
        'pivot_by_day_columns': pivot_by_day_columns,
        'pivot_by_status': pivot_by_status,
    }
    return render(request, 'todo/summary.html', context)


def task_list(request):
    tasks = Task.objects.all().order_by('due_date')
    return render(request, 'todo/task_list.html', {'tasks': tasks})


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/task_form.html', {'form': form})


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/task_form.html', {'form': form})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todo/task_confirm_delete.html', {'task': task})


def export_tasks_csv(request):
    tasks = Task.objects.all().values('title', 'description', 'due_date', 'status', 'priority')
    df = pd.DataFrame(list(tasks))
    
    # Optional: create a pivot table summarizing tasks by status
    pivot = df.pivot_table(index='status', aggfunc='count')
    # (You can log or use the pivot table in a report if desired)
    
    csv_data = df.to_csv(index=False)
    response = HttpResponse(csv_data, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tasks.csv"'
    return response


def dashboard(request):
    # Get task data and use Pandas to generate summary statistics
    tasks = Task.objects.all().values('status', 'due_date')
    df = pd.DataFrame(list(tasks))
    if not df.empty:
        # Count tasks by status using Pandas
        status_summary = df['status'].value_counts().to_dict()
    else:
        status_summary = {}
    
    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(status='Completed').count()
    pending_tasks = Task.objects.filter(status='Pending').count()
    
    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'summary': status_summary,
    }
    return render(request, 'todo/dashboard.html', context)
