from django.urls import path
from . import views

urlpatterns = [
    path("hospital/", views.HospitalView.as_view()),
    path("hospital/", views.HospitalCreateView.as_view()),
    path("hospital/<int:pk>", views.HospitalDetailView.as_view())
]