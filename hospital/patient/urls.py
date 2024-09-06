from .models import Patient
from django.urls import path
from .views import *

urlpatterns = [
    path("token/", Login.as_view()),
    path("token/refresh/", Refresh.as_view()),
    path('new-patinet/' , PatientView.as_view()),
]
