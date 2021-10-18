from django.db import models

from users.models import User
from companies.models import Company


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    patronymic = models.CharField(max_length=15)
    age = models.IntegerField()

    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")

    def __str__(self):
        return f"<Employee {self.surname} {self.name} {self.patronymic}>"


class EmployeeSkill(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    skill = models.CharField(max_length=15)
    skill_level = models.PositiveSmallIntegerField(null=True)

    class Meta:
        verbose_name = ("EmployeeSkill")
        verbose_name_plural = ("EmployeeSkills")

    def __str__(self):
        return f"<Skill {self.skill} of {self.employee.surname} {self.employee.name} {self.employee.patronymic}"


class EmployeeLanguage(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    language = models.CharField(max_length=15)
    language_level = models.CharField(max_length=2)

    def __str__(self):
        return f"<{self.language} {self.language_level} {self.employee.surname} {self.employee.name} {self.employee.patronymic}>"


class EmployeeCompany(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    position = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = ("EmployeeCompany")
        verbose_name_plural = ("EmployeeCompanies")

    def __str__(self):
        return f"<{self.employee.name} {self.employee.patronymic} {self.company} {self.position}>"
