from django.urls import include, path
from rest_framework import routers, urlpatterns

from employees.api.views import EmployeeViewSet

router = routers.DefaultRouter()
router.register(r"employees-api", EmployeeViewSet)

app_name = "employees"
urlpatterns = [
    path('', include(router.urls)),
    path('create/', EmployeeViewSet.as_view({'post': 'create'}), name='employee-create'),
]