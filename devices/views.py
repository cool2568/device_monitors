from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView

from .models import Device
from .serializers import DeviceSerializer

class DeviceListAPIView(ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class=DeviceSerializer 

class DeviceUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer