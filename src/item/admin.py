from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    # list_editable = ('name',)  # which displayed fields are editable in list view
    # list_display_links = ('id', 'name')  # which fields link to detail view
    list_filter = ('name',)
    search_fields = ('name', 'description')
    ordering = ('id',)