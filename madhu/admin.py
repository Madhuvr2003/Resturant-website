from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
    fields = ('name', 'description', 'price')
    readonly_fields = ('created_at',)

admin.site.register(Item, ItemAdmin)
