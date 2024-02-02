from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    # You might want to include the owner's username to display who created the task
    owner_username = serializers.ReadOnlyField(source='assigned_to.user.username')
    is_owner = serializers.SerializerMethodField()
    

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request and obj.assigned_to.user == request.user

    def create(self, validated_data):
        return Task.objects.create(**validated_data, assigned_to=self.context['request'].user.profile)

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'status', 'priority', 'due_date', 
            'created_at', 'updated_at', 'assigned_to', 'owner_username', 'is_owner'
        ]
        extra_kwargs = {
            'assigned_to': {'read_only': True}
        }
