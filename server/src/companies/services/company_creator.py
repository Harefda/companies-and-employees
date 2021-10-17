from companies.models import (
    Company,
    CompanyOffice,
    CompanyCollaboration
)
from app.errors import ObjectAlreadyExists


class CompanyCreator:
    def __init__(self, name, user):
        self.name = name
        self.user = user

    def __call__(self):
        if self.allowed_to_create:
            return self.create()
        else:
            return False

    def create(self):
        return Company.objects.create(
            name=self.name,
            user=self.user
        )

    def allowed_to_create(self, raise_exception=True):
        try:
            if Company.objects.filter(name=self.name).exists():
                raise ObjectAlreadyExists
        except ObjectAlreadyExists as exc:
            if raise_exception:
                return exc
            else:
                return False

        return True


class CompanyOfficeCreator:
    def __init__(self, company, location):
        self.company = company
        self.location = location

    def __call__(self):
        return self.create()

    def create(self):
        return CompanyOffice.objects.create(
            company=self.company,
            location=self.location
        )
