from django.contrib import admin

from employees.models import Employee, EmployeeSkill, EmployeeCompany


admin.site.register(Employee)
admin.site.register(EmployeeSkill)
admin.site.register(EmployeeCompany)
