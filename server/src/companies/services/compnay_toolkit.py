from companies.models import (
    Company,
)
from companies.services import (
    CompanyCreator,
)
from employees.models import Employee
from users.models import User


class CompanyToolKit:
    @classmethod
    def create_company(cls, name, user):
        company = CompanyCreator(
            name=name,
            user=user
        )()
        return company

    @classmethod
    def delete_company(cls, id):
        if Company.objects.filter(id=id).exists():
            company = Company.objects.get(id=id)
            user = User.objects.get(company=company)
            user.is_active = False
            user.save()
        else:
            raise Company.DoesNotExist()

    @classmethod
    def get_company_employees(cls, company):
        employees = Employee.objects.filter(company=company)
        return employees
    