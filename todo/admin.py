from django.contrib import admin

from todo.models import TodoModel

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'term', 'priority', 'status')
    list_filter = ('priority', 'status')
    search_fields = ('title',)
    list_editable = ('priority', 'status')
    
    
admin.site.register(TodoModel, TodoAdmin)