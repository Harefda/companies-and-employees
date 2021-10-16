from django.db import models
from django.db.models.deletion import CASCADE
import employees

from users.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    patronymic = models.CharField(max_length=15)
    age = models.IntegerField(max_length=3)
    #company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"<Employee {self.name, self.surname, self.patronymic}>"


class EmployeeSkills(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    #compnay = models.ForeignKey(Company, on_delete=models.CASCADE)
    skill = models.CharField(max_length=15)
    skill_level = models.IntegerField(max_length=2)

    def __str__(self):
        return f"<Skills of {self.employee.name, self.employee.surname, self.employee.patronymic}"


class EmployeeCompany(models.Model):
    employees = models.ForeignKey(Employee, on_delete=models.CASCADE)
    #company = models.ForeignKey(Company, on_delete=models.CASCADE)
