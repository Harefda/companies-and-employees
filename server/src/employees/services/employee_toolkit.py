from employees.models import(
    Employee,
    EmployeeLanguage,
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

    @classmethod
    def create_employee_skill(cls, employee, skill, skill_level):
        employee_skill = EmployeeSkill.objects.create(
            employee = employee,
            skill = skill,
            skill_level = skill_level
        )
        return employee_skill

    @classmethod 
    def create_employee_language(cls, employee, language, language_level):
        employee_language = EmployeeLanguage.objects.create(
            employee = employee,
            language = language,
            language_level = language_level
        )
        return employee_language

    @classmethod
    def create_employee_company(cls, employee, company, position):
        if not EmployeeCompany.objects.filter(employee=employee, company=company, position=position).exists():
            employee_job = EmployeeCompany.objects.create(
                employee=employee,
                company=company,
                position=position
            )
            return employee_job
        else:
            return False
