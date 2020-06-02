from django.contrib import admin
from .models import Beer, Batch

# Register your models here.

class BatchInline(admin.TabularInline):
    show_change_link = True
    verbose_name = 'Batch'
    verbose_name_plural = 'Batches'
    extra = 0
    model = Batch
    fields = ('brew_date', 'og', 'fg')
    
    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def has_delete_permission(self, request, obj=None) -> bool:
        return False

class LogAdmin(admin.ModelAdmin):
    inlines= [
            BatchInline
            ]

admin.site.register(Beer, LogAdmin)
admin.site.register(Batch)
