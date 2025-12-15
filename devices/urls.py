from django.urls import path
from .views import DeviceListAPIView,DeviceUpdateAPIView

urlpatterns =[
    path("device/",DeviceListAPIView.as_view(),name="device-list"),
    path("device/<int:pk>/", DeviceUpdateAPIView.as_view(), name="device-update"),
]
