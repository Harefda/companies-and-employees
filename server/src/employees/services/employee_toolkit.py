from employees.models import(
    Employee,
    EmployeeSkill,
    EmployeeCompany
)
from employees.services import EmployeeCreator


class EmployeeToolKit:
    @classmethod
    def create_employee(
        cls,
        user,
        name,
        surname,
        patronymic,
        age,
    ):
        employee = EmployeeCreator(
            user=user,
            name=name,
            surname=surname,
            patronymic=patronymic,
            age=age,
        )()
        return employee