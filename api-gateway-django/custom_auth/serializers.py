from rest_framework import serializers

from rest_framework_jwt.settings import api_settings

from custom_auth.models import User, Role
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
import logging
logging.basicConfig(level=logging.INFO)

class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField(default=None, read_only=True)
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255, write_only=True)
    password_confirmation = serializers.CharField(max_length=255, write_only=True)
    role = serializers.CharField(max_length=10, write_only=True)

    def create(self, validated_data):
        if validated_data['password'] != validated_data['password_confirmation']:
            raise serializers.ValidationError({'password': 'Passwords do not match'})

        del validated_data['password_confirmation']

        if validated_data['role'] not in [role.value for role in Role]:
            raise serializers.ValidationError({'role': 'Invalid role'})

        if validated_data['role'] == 'ADMIN':
            del validated_data['role']
            user = User.objects.create_superuser(**validated_data)
        else:
            validated_data['role'] = Role[validated_data['role']]
            user = User.objects.create_user(**validated_data)

        return user

    def update(self, instance, validated_data):
        if validated_data['password'] != validated_data['password_confirmation']:
            raise serializers.ValidationError({'password': 'Passwords do not match'})

        del validated_data['password_confirmation']

        if validated_data['role'] not in [role.value for role in Role]:
            raise serializers.ValidationError({'role': 'Invalid role'})

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.role = validated_data.get('role', instance.role)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_admin = validated_data.get('is_admin', instance.is_admin)

        instance.save()
        return instance
