from django.contrib import admin

from employees.models import Employee, EmployeeSkills, EmployeeCompany


admin.site.register(Employee)
admin.site.register(EmployeeSkills)
admin.site.register(EmployeeCompany)
