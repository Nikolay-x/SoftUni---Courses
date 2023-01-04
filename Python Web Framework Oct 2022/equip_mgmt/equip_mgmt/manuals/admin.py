from django.contrib import admin

from equip_mgmt.manuals.models import Manual


# Register your models here.


@admin.register(Manual)
class ManualAdmin(admin.ModelAdmin):
    list_display = ('name', 'manual_url', 'pump',)
    list_filter = ('pump',)
    search_fields = ('name',)
