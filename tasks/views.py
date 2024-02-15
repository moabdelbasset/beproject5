from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from beproject5.permissions import IsOwnerOrReadOnly
from django.http import Http404


class TaskList(generics.ListCreateAPIView):
    """List or create tasks if logged in"""
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all()

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Task.objects.filter(assigned_to=self.request.user.profile)
        else:
            raise Http404

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(assigned_to=user_profile)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """Provides methods for operations on a single task instance."""
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Task.objects.all()

    def get_serializer_context(self):
        """Provides context for the serializer to use when processing
        requests"""
        context = super().get_serializer_context()
        return context
