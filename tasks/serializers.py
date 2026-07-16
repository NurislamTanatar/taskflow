from rest_framework import serializers
from .models import Task, Project


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class SimpleTaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    status = serializers.CharField(max_length=50)


class SimpleProjectSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()