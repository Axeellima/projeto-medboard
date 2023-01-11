from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("employee/", views.EmployeeView.as_view()),
    path("employee/<int:pk>/", views.EmployeeDetailView.as_view),
    path("employee/login/", jwt_views.TokenObtainPairView.as_view()),
]
