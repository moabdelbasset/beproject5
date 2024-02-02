from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from beproject5.permissions import IsOwnerOrReadOnly


class TaskList(generics.ListCreateAPIView):
    """List or create tasks if logged in"""
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # This view should return a list of all tasks
        # for the currently authenticated user.
        # user_profile = self.request.user.profile
        # return Task.objects.filter(assigned_to=user_profile)
        return Task.objects.all()

    def perform_create(self, serializer):
        # Assign the task to the current user's profile.
        serializer.save(assigned_to=self.request.user)
        # serializer.save(assigned_to=self.request.user.profile, context={'request': self.request})


    # def get_serializer_context(self):
    #     """Extra context provided to the serializer class."""
    #     return {'request': self.request}


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    # def get_serializer_context(self):
    #     """Extra context provided to the serializer class."""
    #     return {'request': self.request}

    # def get_queryset(self):
    #     # This view should return a task
    #     # for the currently authenticated user.
    #     user = self.request.user
    #     return Task.objects.filter(assigned_to__user=user)
