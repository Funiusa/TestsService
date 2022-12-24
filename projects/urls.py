from django.urls import path
from . import views


urlpatterns = [
        path("", views.project_index, name="project_index"),
        path("<int:pk>/", views.porject_detail, name="project_detail"),
]
