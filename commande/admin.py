from django.contrib import admin

# Register your models here.
from .models import Commande, CommandeItem


class CommandeItemInline(admin.TabularInline):
    model = CommandeItem
    raw_id_fields = ['product']


class CommandeAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['first_name', 'adress']
    inlines = [CommandeItemInline]
    
admin.site.register(Commande, CommandeAdmin)
admin.site.register(CommandeItem)