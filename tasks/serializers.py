from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    # You might want to include the owner's username to display who created the task
    owner_username = serializers.ReadOnlyField(source='assigned_to.user.username')
    is_owner = SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'status', 'priority', 'due_date', 
            'created_at', 'updated_at', 'assigned_to', 'owner_username', 'is_owner'
        ]
        extra_kwargs = {
            'assigned_to': {'read_only': True}
        }

    def get_is_owner(self, obj):
        request = self.context['request']
        return obj.assigned_to.user == request.user if request else False

        #return request.user == obj.owner    

    def create(self, validated_data):
        # Assuming you want to automatically set the 'assigned_to' field to the user who created the task
        assigned_to = validated_data.pop('assigned_to', None)
        task = Task.objects.create(**validated_data, assigned_to=assigned_to or self.context['request'].user.profile)
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