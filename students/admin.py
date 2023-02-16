from django.contrib import admin

from .models import student

# admin.site.register(student)

@admin.register(student)
class PostAdmin(admin.ModelAdmin):
    list_display = ['studentname', 'department', 'studentage', 'studentmajor', 'campus']

# Register your models here.
