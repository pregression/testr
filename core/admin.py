from django.contrib import admin
from .models import CspReport

class CspReportAdmin(admin.ModelAdmin):
    pass

admin.site.register(CspReport, CspReportAdmin)
