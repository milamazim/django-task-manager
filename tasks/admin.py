from django.contrib import admin
from tasks.models import Task, Status

class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'created_on',)
    search_fields = ('title', 'description', 'status', 'created_on',)

admin.site.register(Task, TaskAdmin)
admin.site.register(Status, StatusAdmin)
