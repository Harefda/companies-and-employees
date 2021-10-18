from django.urls import include, path
from rest_framework import routers, urlpatterns

from companies.api.views import (
    CompanyViewSet,
    CompanyOfficeViewSet,
)


router = routers.DefaultRouter()
router.register(r"companies-api", CompanyViewSet)

app_name = "companies"
urlpatterns = [
    path('', include(router.urls)),
    path('create/', CompanyViewSet.as_view({'post': 'create'}), name='company-create'),
    path('delete/', CompanyViewSet.as_view({'delete': 'delete'}), name='company-delete'),
    path('office/create/', CompanyOfficeViewSet.as_view({'post': 'create'}), name='company_office-create'),
    path('office/delete/', CompanyOfficeViewSet.as_view({'delete': 'delete'}), name='company_office-delete'),
]