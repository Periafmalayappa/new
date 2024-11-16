from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Project, Task, Comment

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser')
    readonly_fields = ('date_joined',)

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.readonly_fields
        return self.readonly_fields + ('is_staff', 'is_superuser')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'status', 'created_date', 'due_date')
    list_filter = ('status', 'owner')
    search_fields = ('title', 'description')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'assigned_to', 'priority', 'status', 'due_date')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'author', 'created_date')
    list_filter = ('author', 'created_date')
    search_fields = ('content',)