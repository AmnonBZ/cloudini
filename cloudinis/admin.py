from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.site_header = 'Cloudini Administration Panel'

UserAdmin.list_display = ('username', 'organization', 'email', 'date_joined', 'is_active', 'is_staff')
added_item = ('organization',)
UserAdmin.list_filter = UserAdmin.list_filter + added_item

class OrganizationDisplay(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name', 'email')

class PolicyDisplay(admin.ModelAdmin):
    list_display = ('name', 'affectedResources')
    list_filter = ('name', 'affectedResources')

class ActivatedPolicyDisplay(admin.ModelAdmin):
    list_display = ('organization', 'policy', 'metadata', 'actionItem')
    list_filter = ('organization', 'policy', 'metadata', 'actionItem')

class ViolationDisplay(admin.ModelAdmin):
    list_display = ('connectedPolicy', 'resourceName')
    list_filter = ('connectedPolicy', 'resourceName')

admin.site.register(CloudiniUser, UserAdmin)
admin.site.register(Organization, OrganizationDisplay)
admin.site.register(Policy, PolicyDisplay)
admin.site.register(ActivatedPolicy, ActivatedPolicyDisplay)
admin.site.register(Violation, ViolationDisplay)

admin.site.unregister(Group)