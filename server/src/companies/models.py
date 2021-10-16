from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=18)

    def __str__(self) -> str:
        return f"<{self.name}>"


class CompanyOffice(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=15)

    def __str__(self) -> str:
        return f"<office of {self.company, self.location}>"


class CompanyCollaboration(models.Model):
    companies = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    