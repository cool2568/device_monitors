from django.contrib import admin
from devices.models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display =("serial_number","name","is_active","created_at")
    search_fields=("serial_number","name")
    list_filter=("is_active",)