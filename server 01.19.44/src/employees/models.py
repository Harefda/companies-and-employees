from django.db import models

from users.models import User
from companies.models import Company


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    patronymic = models.CharField(max_length=15)
    age = models.IntegerField()
    languages = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")

    def __str__(self):
        return f"<Employee {self.name, self.surname, self.patronymic}>"


class EmployeeSkill(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    skill = models.CharField(max_length=15)
    skill_level = models.PositiveSmallIntegerField(null=True)

    class Meta:
        verbose_name = ("EmployeeSkill")
        verbose_name_plural = ("EmployeeSkills")

    def __str__(self):
        return f"<Skills of {self.employee.patronymic} {self.employee.name} {self.employee.surname}"


class EmployeeCompany(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    company = models.OneToOneField(Company, on_delete=models.CASCADE, null=True, blank=True)
    position = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = ("EmployeeCompany")
        verbose_name_plural = ("EmployeeCompanies")

    def __str__(self):
        return f"<{self.employee.patronymic} {self.employee.name} {self.company} {self.position}>"
