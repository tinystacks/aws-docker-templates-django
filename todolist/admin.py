from django.contrib import admin

# Register your models here.
from . import models
class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title",  "created", "due_date")
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
class ItemListAdmin(admin.ModelAdmin):
    list_display = ("title", "content")
admin.site.register(models.TodoList, TodoListAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.ItemList, ItemListAdmin)
