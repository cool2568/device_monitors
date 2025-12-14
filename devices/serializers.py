from rest_framework import serializers
from .models import Device

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = [
            "id",
            "serial_number",
            "name",
            "is_active",
            "created_at",
            "updated_at",
        ]