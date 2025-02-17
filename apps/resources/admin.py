from django.contrib import admin
from .models import HealthResource, ResourceCategory, ResourceCategoryMapping

@admin.register(HealthResource)
class HealthResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'content', 'author__username')
    date_hierarchy = 'created_at'

@admin.register(ResourceCategory)
class ResourceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_filter = ('parent',)
    search_fields = ('name', 'description')

@admin.register(ResourceCategoryMapping)
class ResourceCategoryMappingAdmin(admin.ModelAdmin):
    list_display = ('category', 'resource', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('category__name', 'resource__title')
    date_hierarchy = 'created_at'
