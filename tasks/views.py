from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from beproject5.permissions import IsOwnerOrReadOnly


class TaskList(generics.ListCreateAPIView):
    """List or create tasks if logged in"""
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(assigned_to=user.profile)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Task.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        return context
