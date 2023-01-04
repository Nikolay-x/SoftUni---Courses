from django.contrib import admin

from equip_mgmt.certificates.models import Certificate


# Register your models here.

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'issue_date', 'expiry_date', 'certificate_url', 'pump')
    list_filter = ('name', 'issue_date', 'expiry_date', 'pump')
    search_fields = ('name', )
