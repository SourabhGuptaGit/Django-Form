from django.contrib import admin
from .models import BuildRequestModel

# Register your models here.

@admin.register(BuildRequestModel)
class BuildRequestadmin(admin.ModelAdmin):
    list_display = ('UserName', 'BuildName', 'DisplaySet')
    ordering = ('UserName',)
    search_fields = ("UserName", "BuildName")