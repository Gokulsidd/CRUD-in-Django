from django.contrib import admin
from CrudApp.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list = ['emp_id', 'emp_name', 'emp_age', 'emp_pnumber']


admin.site.register(Employee, EmployeeAdmin)
