from django.contrib import admin

from sales.models import Payment, Sales, SalesDetail


class SalesDetailInline(admin.TabularInline):
    model = SalesDetail


class SalesAdmin(admin.ModelAdmin):
    inlines = [SalesDetailInline]


admin.site.register(Payment)
admin.site.register(Sales, SalesAdmin)
admin.site.register(SalesDetail)
