from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer

class IsOwner(permissions.BasePermission):
    """Custom permission class to allow only task owners to edit/delete."""
    def has_object_permission(self, request, view, obj):
        return obj.assigned_to.user == request.user

class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # This view should return a list of all tasks
        # for the currently authenticated user.
        # user_profile = self.request.user.profile
        # return Task.objects.filter(assigned_to=user_profile)
        return Task.objects.all()

    def perform_create(self, serializer):
        # Assign the task to the current user's profile.
        serializer.save(assigned_to=self.request.user.profile)

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        # This view should return a task
        # for the currently authenticated user.
        user = self.request.user
        return Task.objects.filter(assigned_to__user=user)
