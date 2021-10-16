from django.db import models
from django.db.models.deletion import CASCADE

from users.models import User
from companies.models import Company


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    patronymic = models.CharField(max_length=15)
    age = models.IntegerField()

    def __str__(self):
        return f"<Employee {self.name, self.surname, self.patronymic}>"


class EmployeeSkills(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    compnay = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    skill = models.CharField(max_length=15)
    skill_level = models.PositiveSmallIntegerField(null=True)
    languages = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"<Skills of {self.employee.patronymic} {self.employee.name} {self.employee.surname}"


class EmployeeCompany(models.Model):
    employees = models.OneToOneField(Employee, on_delete=models.CASCADE, null=True, blank=True)
    company = models.OneToOneField(Company, on_delete=models.CASCADE, null=True, blank=True)
    position = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"<{self.employee.patronymic} {self.employee.name} {self.company} {self.position}>"
