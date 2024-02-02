from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from beproject5.permissions import IsOwnerOrReadOnly


class TaskList(generics.ListCreateAPIView):
    """List or create tasks if logged in"""
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
