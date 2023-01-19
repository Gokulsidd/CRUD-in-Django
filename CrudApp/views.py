from django.shortcuts import render, redirect
from CrudApp.models import Employee
from CrudApp.forms import EmployeeForm


def retrieve_employee(request):
    employee = Employee.objects.all()
    return render(request, 'CrudApp/dashboard.html', context={'employee': employee})


def add_employee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    return render(request, 'CrudApp/create.html', context={'form': form})


def update_employee(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    return render(request, 'CrudApp/update.html', {'employee': employee})


def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/dashboard')
