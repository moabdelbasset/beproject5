from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    # You might want to include the owner's username to display who created the task
    owner_username = serializers.ReadOnlyField(source='assigned_to.user.username')
    is_owner = serializers.ReadOnlyField()
    

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def create(self, validated_data):
        # Assuming you want to automatically set the 'assigned_to' field to the user who created the task
        assigned_to = validated_data.pop('assigned_to', None)
        task = Task.objects.create(**validated_data, assigned_to=assigned_to or self.context['request'].user.profile)
        return task

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'status', 'priority', 'due_date', 
            'created_at', 'updated_at', 'assigned_to', 'owner_username', 'is_owner'
        ]
        extra_kwargs = {
            'assigned_to': {'read_only': True}
        }
