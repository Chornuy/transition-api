from django.urls import path

from incometraffic import views

urlpatterns = [
    path("proxy-project/", views.ProjectView.as_view()),
    path("proxy-project/<int:pk>", views.ProjectDetails.as_view()),
    path("send-message/", views.SendMessage.as_view()),
    path("message/<str:pk>", views.ViewMessage.as_view())
]
