from django.urls import path
from . import views

urlpatterns = [
    path("consultation/", views.ConsultationView.as_view()),
    path("consultation/<int:pk>/", views.ConsultationDetailView.as_view),
]
