from django.urls import path
from .views import DeviceListAPIView

urlpatterns =[
    path("device/",DeviceListAPIView.as_view(),name="device-list")
]
