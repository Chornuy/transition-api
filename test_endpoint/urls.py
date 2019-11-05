from django.urls import path

from test_endpoint import views

urlpatterns = [
    path("test/", views.TestApiEndpoint.as_view(), name="test_endpoint"),
]
