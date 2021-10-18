from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from companies.api.serializers import (
    CompanySerializer,
    CompanyOfficeSerializer
)
from app.errors import ObjectAlreadyExists, ValidationError
from companies.services import CompanyToolKit
from companies.models import Company, CompanyOffice
from companies.utils import CompanyErrorMessages


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAdminUser]

    def create(self, request):
        data = request.POST or request.data

        try:
            user = request.user
            name = data["name"]
        except KeyError:
            return Response({"error": CompanyErrorMessages.REQUEST_FIELDS_ERROR.value}, status=400)

        try:
            company = CompanyToolKit.create_company(
                name=name,
                user=user
            )
        except ValidationError as exc:
            return Response({"error": str(exc)}, status=400)
        except ObjectAlreadyExists:
            return Response({"error": CompanyErrorMessages.NON_UNIQUE_COMPANY_NAME_ERROR.value}, status=400)

        serializer = CompanySerializer(instance=company)
        return Response(serializer.data, status=201)

    def delete(self, request):
        data = request.POST or request.data
        try:
            id = data["id"]
        except KeyError:
            return Response({"error": CompanyErrorMessages.REQUEST_FIELDS_ERROR.value}, status=400)

        try:
            CompanyToolKit.delete_company(id=id)
        except Company.DoesNotExist:
            return Response({"error": CompanyErrorMessages.COMPANY_DOES_NOT_EXISTS.value}, status=400)

        return Response({"success": f"Company with id - {id} was deleted"})


class CompanyOfficeViewSet(viewsets.ModelViewSet):
    queryset = CompanyOffice.objects.all()
    serializer_class = CompanyOfficeSerializer
    permission_classes = [IsAdminUser]

    def create(self, request):
        data = request.POST or request.data

        try:
            company = request.user.company
            location = data["location"]
        except KeyError:
            return Response({"error": CompanyErrorMessages.REQUEST_FIELDS_ERROR.value}, status=400)

        try:
            company_office = CompanyToolKit.create_company_office(
                company=company,
                location=location
            )
        except ValidationError as exc:
            return Response({"error": str(exc)}, status=400)
        except:
            return Response({"error": CompanyErrorMessages.NON_UNIQUE_COMPANY_OFFICE_ERROR.value}, status=400)

        serializer = CompanyOfficeSerializer(instance=company_office)
        return Response(serializer.data, status=201)

    def delete(self, request):
        data = request.POST or request.data
        try:
            company = request.user.company
            location = data["location"]
            
        except KeyError:
            return Response({"error": CompanyErrorMessages.REQUEST_FIELDS_ERROR.value}, status=400)

        try:
            CompanyToolKit.delete_company_office(
                company = company,
                location = location
            )
        except CompanyOffice.DoesNotExist:
            return Response({"error": CompanyErrorMessages.COMPANY_OFFICE_DOES_NOT_EXISTS.value}, status=400)

        return Response({"success": f"Company office with id - {id} was deleted"})