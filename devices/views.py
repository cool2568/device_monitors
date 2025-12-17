from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from .pagination import DevicePagination
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsStaffForWrite


from .models import Device
from .serializers import DeviceCreateSerializer,DeviceUpdateSerializer

class DeviceListAPIView(ListCreateAPIView):
    serializer_class = DeviceCreateSerializer
    pagination_class = DevicePagination
    filter_backends =[SearchFilter,OrderingFilter]
    search_fields =['name','serial_number']
    ordering_fields=['created_at','name']
    ordering=['-created_at']

    def get_permission(self):
        if self.request.method == "POST":
            return(IsAdminUser())
        return[IsAuthenticated()]
    
    def get_queryset(self):
        queryset = Device.objects.all()

        is_active = self.request.query_params.get("is_active")

        if is_active is not None:
            if is_active.lower() == "true":
                queryset = queryset.filter(is_active=True)
            elif is_active.lower() == "false":
                queryset = queryset.filter(is_active=False)

        return queryset

        
    serializer_class=DeviceCreateSerializer

class DeviceUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Device.objects.all()
    permission_class =[IsStaffForWrite]
    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return DeviceUpdateSerializer
        return DeviceCreateSerializer

    def put(self,request,*args,**kwargs):
        return Response(
            {"detail":"Put Method is not allowed use Patch"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )