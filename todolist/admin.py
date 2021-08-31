from django.contrib import admin

# Register your models here.
from . import models
class ItemListAdmin(admin.ModelAdmin):
    list_display = ("title", "content")
admin.site.register(models.ItemList, ItemListAdmin)
