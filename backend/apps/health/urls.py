from django.urls import path

from apps.health import views

urlpatterns = [
    path("", views.HealthCheckView.as_view(), name=""),
]
