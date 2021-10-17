from companies.models import (
    Company,
    CompanyOffice
)
from companies.services import (
    CompanyCreator,
    CompanyOfficeCreator
)


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
            Company.objects.filter(id=id).delete()
        else:
            raise Company.DoesNotExist()

    @classmethod
    def create_company_office(cls, company, location):
        company_office =  CompanyOfficeCreator(
            company=company,
            location=location
        )()
        return company_office

    @classmethod
    def delete_company_office(cls, company, location):
        if CompanyOffice.objects.filter(company=company, location=location).exists():
            CompanyOffice.objects.filter(company=company, location=location).delete()
        else:
            raise CompanyOffice.DoesNotExist()

    