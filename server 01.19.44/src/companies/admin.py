from django.contrib import admin

from companies.models import Company, CompanyOffice, CompanyCollaboration


admin.site.register(Company)
admin.site.register(CompanyOffice)
admin.site.register(CompanyCollaboration)
