from django.urls import include, path
from rest_framework import routers, urlpatterns

from employees.api.views import (
    EmployeeLanguageViewSet,
    EmployeeViewSet,
    EmployeeSkillViewSet,
    EmployeeCompanyViewSet
)

router = routers.DefaultRouter()
router.register(r"employees-api", EmployeeViewSet)

app_name = "employees"
urlpatterns = [
    path('', include(router.urls)),
    path('create/', EmployeeViewSet.as_view({'post': 'create'}), name='employee-create'),
    path('<int:id>/delete', EmployeeViewSet.as_view({'delete': 'delete'}), name='employee-delete'),
    path('skill/create/', EmployeeSkillViewSet.as_view({'post': 'create'}), name='employee_skill-create'),
    path('language/create/', EmployeeLanguageViewSet.as_view({'post': 'create'}), name='employee_language-create'),
    path('company/create/', EmployeeCompanyViewSet.as_view({'post': 'create'}), name='employee_company-create')
]