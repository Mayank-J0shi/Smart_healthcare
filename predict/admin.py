from django.contrib import admin
from .models import database, doc_DB, Report
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

class ReportAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
class databaseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
class doc_DBAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(database, databaseAdmin)
admin.site.register(doc_DB, doc_DBAdmin)
admin.site.register(Report, ReportAdmin)

