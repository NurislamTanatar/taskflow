from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("create/", views.create_task, name="create_task"),
    path("delete/<int:pk>/", views.delete_task, name="delete_task"),

    path("api/tasks/", views.api_tasks, name="api_tasks"),
    path("api/tasks/<int:pk>/", views.TaskDetailAPIView.as_view(), name="task_detail"),

    path("api/tasks/class/", views.TaskListAPIView.as_view(), name="api_tasks_class"),
    path("api/projects/", views.api_projects, name="api_projects"),
    path("api/projects/class/", views.ProjectListAPIView.as_view(), name="project_api"),
]