from django.contrib import admin
from api.models import Company, Employee

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','location','type')
    search_fields = ('name','location')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','position','company')
    list_filter = ('company',)

admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
