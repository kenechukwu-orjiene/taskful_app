from django.contrib.auth.models import User
from rest_framework import serializers
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name='user-detail')

    class Meta:
        model = Profile 
        fields = ['url', 'id', 'user', 'image']

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=False)
    old_password = serializers.CharField(write_only=True, required=False)
    username = serializers.CharField(read_only=True)
    profile = ProfileSerializer(read_only=True)

    def validate(self, data):
        request_method = self.context['request'].method
        password = data.get('password', None)
        if password == None:
            raise serializers.ValidationError({'error': "please provide password."})
        elif request_method == 'PUT' or request_method == "PATCH":
            old_password = data.get('old_password', None)
            if password != None and old_password == None:
                raise serializers.ValidationError({'error': "please provide old password."})
        return data

    def create(self, validate_data):
        password = validate_data.pop('password')
        user = User.objects.create(**validate_data)
        user.set_password(password)
        user.save()

        return user
    
    def update(self, instance, validate_data):
        try:
            user = instance
            if 'password' in validate_data:
                password = validate_data.pop('password')
                old_password = validate_data.pop('old_password')
                if user.check_password(old_password):
                    user.set_password(password)
                else:
                    raise Exception('Old password is wrong. Check again')
                user.save()
        except Exception as e:
            raise serializers.ValidationError({'info': e})
        
        return super(UserSerializer, self).update(instance, validate_data)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'first_name', 'last_name', 'password', 'old_password', 'profile']