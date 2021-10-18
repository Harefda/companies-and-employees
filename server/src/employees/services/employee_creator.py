from employees.models import Employee
from app.errors import ObjectAlreadyExists


class EmployeeCreator:
    def __init__(
        self,
        user,
        name,
        surname,
        patronymic,
        age,
    ):
        self.user = user
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.age = age

    def __call__(self):
        if self.allowed_to_create():
            return self.create_employee()

    def create_employee(self):
        return Employee.objects.create(
            user=self.user,
            name=self.name,
            surname=self.surname,
            patronymic=self.patronymic,
            age=self.age,
        )

    def allowed_to_create(self, raise_exception=True):
        try:
            if Employee.objects.filter(user=self.user):
                raise ObjectAlreadyExists
        except ObjectAlreadyExists as exc:
            if raise_exception:
                raise exc
            else:
                return False

        return True