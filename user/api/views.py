from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from user.models import Profile
from django.contrib.auth.models import User
from user.api.serializers import UserSerializer, ProfileSerializer
import coreapi
from rest_framework.schemas import AutoSchema
from rest_framework.views import APIView

from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class UserViewSchema(AutoSchema):

    def get_manual_fields(self, path, method):
        extra_fields = []
        if method in ['POST', 'PUT']:
            extra_fields = [
                coreapi.Field('username'),
                coreapi.Field('first_name'),
                coreapi.Field('last_name'),
                coreapi.Field('email'),
                coreapi.Field('password'),
                coreapi.Field('timezone'),
            ]
            manual_fields = super().get_manual_fields(path, method)
            return manual_fields + extra_fields


# class UserCollection(APIView):

#     schema = UserViewSchema()

#     def get(self, request):
#         try:
#             user = User.objects.all()
#             profile = Profile.objects.all()
#         except User.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

    
#         if request.method == 'GET':
#             serializer = UserSerializer(user, many=True)
#             serializer2 = ProfileSerializer(profile, many=True)
#             return Response(serializer.data+serializer2.data)

#     def post(self, request):    
#         if request.method == 'POST':
#             username = request.data['username']
            
#             if User.objects.filter(username=username).exists():
#                 return Response(f'username {username} already exists')
            
#             first_name = request.data['first_name']
#             last_name = request.data['last_name']
#             password = request.data['password']
#             timezone = request.data['timezone']

#             if len(password) not in range(4,20):
#                 return Response(f'Entered password is not valid. password length should be in between 4 and 20')

#             email = request.data['email']

#             try:
#                 validate_email(email)
#             except ValidationError as e:
#                 return Response("Enter valid email address")

            
            
#             user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password, email=email)
#             Profile.objects.create(user=user, timezone=timezone, is_talent=True)
#             return Response(status=status.HTTP_201_CREATED)

class FanCollection(APIView):

    schema = UserViewSchema()

    def get(self, request):
        try:
            profile = Profile.objects.filter(is_talent=False)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    
        if request.method == 'GET':
            serializer = ProfileSerializer(profile, many=True)
            return Response(serializer.data)

    def post(self, request):
        if request.method == 'POST':
            username = request.data['username']
            if User.objects.filter(username=username).exists():
                return Response(f'username {username} already exists')
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            password = request.data['password']

            if len(password) not in range(4,20):
                return Response(f'Entered password is not valid. password length should be in between 4 and 20')

            email = request.data['email']

            try:
                validate_email(email)
            except ValidationError as e:
                return Response("Enter valid email address")

            timezone = request.data['timezone']
            
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password, email=email)
            Profile.objects.create(user=user, timezone=timezone, is_talent=False)
            return Response(status=status.HTTP_201_CREATED)


class TalentCollection(APIView):
    schema = UserViewSchema()

    def get(self, request):
        try:
            profile = Profile.objects.filter(is_talent=True)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        if request.method == 'GET':
            serializer = ProfileSerializer(profile, many=True)
            return Response(serializer.data)

    def post(self, request):
        
        if request.method == 'POST':
            username = request.data['username']
            if User.objects.filter(username=username).exists():
                return Response(f'username {username} already exists')
            
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            password = request.data['password']

            if len(password) not in range(4,20):
                return Response(f'Entered password is not valid. password length should be in between 4 and 20')

            email = request.data['email']

            try:
                validate_email(email)
            except ValidationError as e:
                return Response("Enter valid email address")

            timezone = request.data['timezone']
            
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password, email=email)
            Profile.objects.create(user=user, timezone=timezone, is_talent=True)
            return Response(status=status.HTTP_201_CREATED)


