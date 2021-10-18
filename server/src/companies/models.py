from django.db import models

from users.models import User


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=18)

    class Meta:
        verbose_name = ("Company")
        verbose_name_plural = ("Companies")

    def __str__(self) -> str:
        return f"<{self.name}>"


class CompanyOffice(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=15)

    def __str__(self) -> str:
        return f"<{self.location} {self.company}>"


class CompanyCollaboration(models.Model):
    collaboration_name = models.CharField(max_length=15, null=True, blank=True)
    companies = models.ManyToManyField(Company, blank=True)

    def __str__(self):
        return f"<{self.collaboration_name}>"
    