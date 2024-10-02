from rest_framework import serializers

from house.models import House

class HouseSerializer(serializers.ModelSerializer):
    members_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = House
        fields = ['url', 'id', 'image', 'name', 'created_on',
                  'manager', 'members_count', 'description','points',
                  'completed_tasks_count', 'noncompleted_tasks_count']
        read_only_fields = ['points', 'completed_tasks_count', 'noncompleted_tasks_count']
