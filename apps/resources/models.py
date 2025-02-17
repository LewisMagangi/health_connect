from django.db import models
from django.conf import settings

class HealthResource(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'resources_health_resource'
        verbose_name = 'Health Resource'
        verbose_name_plural = 'Health Resources'

class ResourceCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    resources = models.ManyToManyField(HealthResource, through='ResourceCategoryMapping')

    class Meta:
        db_table = 'resources_category'
        verbose_name = 'Resource Category'
        verbose_name_plural = 'Resource Categories'

    def __str__(self):
        return self.name

class ResourceCategoryMapping(models.Model):
    category = models.ForeignKey(ResourceCategory, on_delete=models.CASCADE)
    resource = models.ForeignKey(HealthResource, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'resources_category_mapping'
        unique_together = ('category', 'resource')
        verbose_name = 'Resource Category Mapping'
        verbose_name_plural = 'Resource Category Mappings'
