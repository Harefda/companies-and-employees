from rest_framework import serializers

from employees.models import (
    Employee,
    EmployeeSkill,
    EmployeeLanguage,
    EmployeeCompany
)


class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields = [
            'id',
            'user',
            'name',
            'surname',
            'patronymic',
            'age'
        ]


class EmployeeSkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeSkill
        fields = [
            'employee',
            'skill',
            'skill_level'
        ]