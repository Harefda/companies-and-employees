from django.contrib import admin

from employees.models import (
    Employee,
    EmployeeSkill,
    EmployeeLanguage,
    EmployeeCompany
)


admin.site.register(Employee)
admin.site.register(EmployeeSkill)
admin.site.register(EmployeeLanguage)
admin.site.register(EmployeeCompany)
