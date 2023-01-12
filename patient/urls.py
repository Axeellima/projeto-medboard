from django.urls import path
from . import views

urlpatterns = [
    path("patient/", views.PatientView.as_view()),
    path("patient_code/<str:patient_code>/", views.PatientCodeView.as_view()),
    path("patient/<int:pk>/", views.PatientIdView.as_view()),
]
