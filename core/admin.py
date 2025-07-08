from django.contrib import admin
from .models import Property, PropertyImageInline, PropertyDocumentInline

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'property_type', 'zone', 'price', 'location', 'is_verified', 'is_active', 'created_at']
    list_filter = ['property_type', 'zone', 'is_verified', 'is_active', 'created_at']
    search_fields = ['title', 'location', 'owner__full_name', 'owner__phone']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [PropertyImageInline, PropertyDocumentInline] 