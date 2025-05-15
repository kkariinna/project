from django.contrib import admin
from .models import Abc

# Register your models here.

# admin.site.register(Abc)
@admin.register(Abc)
class AbcAdmin(admin.ModelAdmin):
    list_display = ['id', 'task', 'a', 'b', 'c', 'current_date']
    list_editable = ['task', 'a', 'b', 'c']
    search_fields = ['task', 'a', 'b', 'c']
    list_filter = ['task', 'a', 'b', 'c']
    list_per_page = 15


