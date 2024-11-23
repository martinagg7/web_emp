from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')  # Campos de solo lectura
    list_display = ('title', 'order')  # Campos mostrados en la lista

admin.site.register(Page, PageAdmin)