
# _*_ coding=utf8 _*_

from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('sex','birthday')

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    class Meta:
        model = User
        fields = ('username','password','first_name','last_name','email','profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self,validated_data):
        user = User(username=validated_data['username'],first_name=validated_data['first_name'],last_name=validated_data['last_name'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        profile_data = validated_data.pop('profile')
        profile = Profile.objects.create(user=user,sex=profile_data['sex'],birthday=profile_data['birthday'])
        return user

    def update(self,instance,validated_data):
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.save()
        
        profile_data = validated_data.pop('profile')
        profile = instance.profile 
        profile.sex = profile_data['sex']
        profile.birthday = profile_data['birthday']
        profile.save()
        
        return instance

