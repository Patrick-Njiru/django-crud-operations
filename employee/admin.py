from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ['eid', 'name', 'contact', 'email']
    search_fields = ["name"]

admin.AdminSite.site_header, admin.AdminSite.site_title = "Employees Administration", "Employees"