from django.urls import path, include
from projects import views

urlpatterns = [
    path("", views.projects, name="projects"),
    path("project/<str:pk>", views.project, name="project"),
]
