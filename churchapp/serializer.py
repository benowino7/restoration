# type:ignore
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

'''
    User serializer class
'''
User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        many=True
        model = User
        fields =  ['id','username','email','phone','role']
