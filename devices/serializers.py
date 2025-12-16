from rest_framework import serializers
from .models import Device


class DeviceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model =Device
        fields="__all__"
        read_only_fields=(
            "id",
            "serial_number",
            "name",
            "created_at",
            "updated_at",

        )
    
    def validate_serial_number(self,value):
        queryset=Device.objects.filter(serial_number=value)

        if self.instance:
            queryset=queryset.exclude(id=self.instance.id)

            if queryset.exists():
                raise serializers.ValidationError(
                    "Device with this serial number already exists."
                )
            return value
    

class DeviceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Device
        field=('is_active','name')

    def validate(self,attrs):
        if not attrs:
            raise serializers.ValidationError(
                {"detail":"No validate fields provide for update"}
            )
        return attrs
    
    
    def update(self,instance,validated_data):
        instance.is_active=validated_data.get("is_active")
        instance.save()
        return instance


    