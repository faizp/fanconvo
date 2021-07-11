from rest_framework import serializers
from user.models import Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField('get_username')
    first_name = serializers.SerializerMethodField('get_first_name')
    last_name = serializers.SerializerMethodField('get_last_name')
    email = serializers.SerializerMethodField('get_email')
    password = serializers.SerializerMethodField('get_password')

    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'timezone']

    def get_username(self, profile):
        username = profile.user.username
        return username

    def get_first_name(self, profile):
        first_name = profile.user.first_name
        return first_name

    def get_last_name(self, profile):
        last_name = profile.user.last_name
        return last_name

    def get_email(self, profile):
        email = profile.user.email
        return email

    def get_password(self, profile):
        password = profile.user.password
        return password 