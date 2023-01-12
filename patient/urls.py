from django.urls import path
from . import views

urlpatterns = [
    path("patient/", views.PatientView.as_view()),
    path("patient/<str:patient_code>/", views.PatientCodeView.as_view()),
    path("patient/<int:patient_id>/", views.PatientIdView.as_view()),
]
