from django.urls import path
from . import views

urlpatterns = [
        path("contact/", views.ContactView.as_view()),
        path("contact/<int:pk>", views.ContactDetailView.as_view)
]
