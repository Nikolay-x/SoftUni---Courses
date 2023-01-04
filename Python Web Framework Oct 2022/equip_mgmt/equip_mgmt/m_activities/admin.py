from django.contrib import admin

from equip_mgmt.m_activities.models import Activity


# Register your models here.

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('description', 'due_date', 'status', 'pump',)
    list_filter = ('due_date', )
    search_fields = ('description',)
