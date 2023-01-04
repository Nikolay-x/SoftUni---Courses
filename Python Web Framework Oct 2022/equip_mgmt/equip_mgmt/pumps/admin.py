from django.contrib import admin

from equip_mgmt.pumps.models import Pump


# Register your models here.


@admin.register(Pump)
class PumpAdmin(admin.ModelAdmin):
    list_display = ('tag', 'name', 'type', 'model', 'fluid', 'flow_rate', 'head', 'power', 'image_url')
    list_filter = ('tag',)
    search_fields = ('tag', 'fluid')
