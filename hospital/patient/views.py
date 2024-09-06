from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializer import *
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
class Login(TokenObtainPairView):
    pass

class Refresh(TokenRefreshView):
    pass


class PatientView(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]