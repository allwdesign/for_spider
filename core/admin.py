from django.contrib import admin
from .models import District, Category, Service, Organization


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'category', 'price')

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('organization_name', 'description',)
    filter_horizontal = ('districts', 'services')


admin.site.register(District)
admin.site.register(Category)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Organization, OrganizationAdmin)
