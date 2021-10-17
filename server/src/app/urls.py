from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/", include("users.urls", namespace="users")),
    path("company/", include("companies.urls", namespace="companies"))
]