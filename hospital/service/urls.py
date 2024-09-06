from django.urls import path
from .views import *

urlpatterns = [
    path("list-service/", ServiceView.as_view()),
    path("super-list-serive/", SuperUserView.as_view()),
    path("new-service/ ", ServiceView.as_view()),
]
