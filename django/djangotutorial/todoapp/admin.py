from django.contrib import admin
from .models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'completed', 'created_at']
    list_filter = ['completed', 'created_at', 'user']
    search_fields = ['title', 'description']
    
admin.site.register(Todo, TodoAdmin)