from rest_framework import serializers

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