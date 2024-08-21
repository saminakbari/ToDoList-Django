from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from ToDoListApp.models import Task
from ToDoListApp.serializers import TaskSerializer


class TaskViewSet(viewsets.ViewSet):
    def list(self, request, **kwargs):
        user_to_do_lists = request.user.to_do_lists.all()
        to_do_list = user_to_do_lists.get(pk=self.kwargs['list_id'])
        queryset = filter(lambda task: task in to_do_list.tasks.all(),
                          Task.objects.filter(owner=request.user))
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            user_to_do_lists = request.user.to_do_lists.all()
            to_do_list = user_to_do_lists.get(pk=self.kwargs['list_id'])
            task.to_do_lists.add(to_do_list)
            task.user = request.user
            task.save()
            return Response("Task created successfully.")
        else:
            return Response("Invalid data.")

    def retrieve(self, request, task_id=None):
        queryset = Task.objects.filter(owner=request.user)
        task = get_object_or_404(queryset, pk=task_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)