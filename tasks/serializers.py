from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    # You might want to include the owner's username to display who created the task
    owner_username = serializers.ReadOnlyField(source='assigned_to.user.username')

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'status', 'priority', 'due_date', 
            'created_at', 'updated_at', 'assigned_to', 'owner_username'
        ]
        extra_kwargs = {
            'assigned_to': {'read_only': True}
        }

    def create(self, validated_data):
        # Assuming you want to automatically set the 'assigned_to' field to the user who created the task
        task = Task.objects.create(**validated_data, assigned_to=self.context['request'].user.profile)
        return task





# from rest_framework import serializers
# from .models import Profile

# class ProfileSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#     is_owner = serializers.SerializerMethodField()

#     def get_is_owner(self, obj):
#         request = self.context['request']
#         return request.user == obj.owner

#     class Meta:
#         model = Profile
#         fields = [
#             'id', 'owner', 'name', 'image', 'is_owner'
#         ]