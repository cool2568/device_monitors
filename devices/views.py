from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from .models import Device
from .serializers import DeviceSerializer

class DeviceListAPIView(ListAPIView):
    queryset = Device.objects.all()
    serializer_class=DeviceSerializer 