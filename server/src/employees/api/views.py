from django.utils.decorators import sync_and_async_middleware
from rest_framework import serializers, status, viewsets
from rest_framework.response import Response
from companies.models import Company

from employees.api.serializers import (
    EmployeeSerializer,
    EmployeeSkillSerializer,
    EmployeeLanguageSerializer,
    EmployeeCompanySerializer
)
from app.errors import ValidationError
from employees.services import EmployeeToolKit
from employees.utils import EmployeeErrorMessages
from employees.models import (
    Employee,
    EmployeeSkill,
    EmployeeLanguage,
    EmployeeCompany
)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request):
        data = request.POST or request.data

        try:
            user = request.user
            name = data["name"]
            surname = data["surname"]
            patronymic = data["patronymic"]
            age = data["age"]
        except KeyError:
            return Response({"error": EmployeeErrorMessages.REQUEST_FIELDS_ERROR.value}, status=400)

        try:
            employee = EmployeeToolKit.create_employee(
                user=user,
                name=name,
                surname=surname,
                patronymic=patronymic,
                age=age,
            )
        except ValidationError as exc:
            return Response({"error": str(exc)}, status=400)
        
        serializer = EmployeeSerializer(instance=employee)
        return Response(serializer.data, status=201)


class EmployeeSkillViewSet(viewsets.ModelViewSet):
    queryset = EmployeeSkill.objects.all()
    serializer_class = EmployeeSkillSerializer

    def create(self, request):
        data = request.POST or request.data

        try:
            employee = request.user.employee
            skill = data["skill"]
            skill_level = data["skill_level"]
        except KeyError:
            return Response({"error": EmployeeErrorMessages.REQUEST_FIELDS_ERROR.value}, status=400)

        try:
            employee_skill = EmployeeToolKit.create_employee_skill(
                employee=employee,
                skill=skill,
                skill_level=skill_level
            )
        except ValidationError as exc:
            return Response({"error": str(exc)}, status=400)

        serializer = EmployeeSkillSerializer(instance=employee_skill)
        return Response(serializer.data, status=201)


class EmployeeLanguageViewSet(viewsets.ModelViewSet):
    queryset = EmployeeLanguage.objects.all()
    serializer_class = EmployeeLanguageSerializer

    def create(self, request):
        data = request.POST or request.data

        try:
            employee = request.user.employee
            language = data["language"]
            language_level = data["language_level"]
        except KeyError:
            return Response({"error": EmployeeErrorMessages.REQUEST_FIELDS_ERROR.value}, status=400)

        try:
            employee_language = EmployeeToolKit.create_employee_language(
                employee=employee,
                language=language,
                language_level=language_level
            )
        except ValidationError as exc:
            return Response({"error": str(exc)}, status=400)

        serializer = EmployeeLanguageSerializer(instance=employee_language)
        return Response(serializer.data, status=201)


class EmployeeCompanyViewSet(viewsets.ModelViewSet):
    queryset = EmployeeCompany.objects.all()
    serializer_class = EmployeeCompanySerializer

    def create(self, request):
        data = request.POST or request.data

        try:
            employee = request.user.employee
            company = Company.objects.get(name=data["company"])
            position = data["position"]
        except KeyError:
            return Response({"error": EmployeeErrorMessages.REQUEST_FIELDS_ERROR.value}, status=400)

        try:
            employee_company = EmployeeToolKit.create_employee_company(
                employee = employee,
                company = company,
                position = position
            )
        except ValidationError as exc:
            return Response({"error": str(exc)}, status=400)
        
        serializer = EmployeeCompanySerializer(instance=employee_company)
        return Response(serializer.data, status=201)
