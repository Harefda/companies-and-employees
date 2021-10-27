from django.urls import include, path
from rest_framework import routers, urlpatterns

from companies.api.views import (
    CompanyViewSet,
    CompanyOfficeViewSet,
)


router = routers.DefaultRouter()
router.register(r"companies-api", viewset=CompanyViewSet, basename="company")
router.register(r"company_offices-api", CompanyOfficeViewSet)

app_name = "companies"
urlpatterns = [
    path('', include(router.urls)),
    path('create/', CompanyViewSet.as_view({'post': 'create'}), name='company-create'),
    path('<int:id>/delete/', CompanyViewSet.as_view({'delete': 'delete'}), name='company-delete'),
    path('employees/amount/get', CompanyViewSet.as_view({'get': 'get_amount_of_employees'}), name='company_employees_amount-get'),
    path('employees/get/', CompanyViewSet.as_view({'get': 'get_employees'}), name='company_employees-get'),
    path('office/create/', CompanyOfficeViewSet.as_view({'post': 'create'}), name='company_office-create'),
    path('office/delete/', CompanyOfficeViewSet.as_view({'delete': 'delete'}), name='company_office-delete'),
]