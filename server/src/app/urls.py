from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Swagger')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('users.urls', namespace='users')),
    path('company/', include('companies.urls', namespace='companies')),
    path('employee/', include('employees.urls', namespace='employees')),
    path('', schema_view)
]