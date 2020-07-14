from django.contrib import admin
from .models import Payment
from import_export.admin import ImportExportModelAdmin

@admin.register(Payment)
class PaymentAdmin(ImportExportModelAdmin):
    list_display = ('title','value','date','externalTax', 'comment')
# admin.site.register(Payment)