from django.contrib import admin

from .models import Estimate, Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("address", "lot_size_acres", "created_at")


@admin.register(Estimate)
class EstimateAdmin(admin.ModelAdmin):
    list_display = ("project_name", "inquiry", "net_cash_flow", "created_at")
