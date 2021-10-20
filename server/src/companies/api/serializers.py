from django.db import models
from django.db.models import fields
from rest_framework import serializers

from employees.models import EmployeeCompany
from companies.models import (
    Company,
    CompanyOffice,
    CompanyCollaboration
)


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = [
            'name',
            'id'
        ]

 
class CompanyOfficeSerializer(serializers.ModelSerializer):

     class Meta:
         model = CompanyOffice
         fields = [
             'company',
             'location'
         ]


class CompanyEmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeCompany
        fields = [
            'employee',
            'company',
            'position'
        ]


class CompanyEmployeesAmountSerializer(serializers.ModelSerializer):
    employees_amount = serializers.SerializerMethodField()

    class Meta:
        model = EmployeeCompany
        fields = [
            'employees_amount'
        ]

    def get_employees_amount(self, obj):
        employees_amount = len(obj)
        return employees_amount