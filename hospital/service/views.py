from .serializer import *
from .models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ServiceView(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]



class ServiceDetail(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]



class SuperUserView(ListAPIView):
    queryset = Reserve.objects.all()
    serializer_class = SuperUserReserveSerializer
    permission_classes = [IsSuperUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['date']


    