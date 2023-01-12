from django.urls import path
from . import views

urlpatterns = [
    path("pathology/", views.PathologyView.as_view()),
]
