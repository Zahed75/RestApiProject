from rest_framework import serializers
from select import error
from django.contrib.auth.models import User
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError({'error': "age should be greater then 18"})

        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({'error': "Name cannot be digit"})
        #
        # if data['department']:
        #     for x in data['department']:
        #         if x is not 'CSE':
        #             raise serializers.ValidationError({'error': 'department name must be CSE'})
        return data


class CategeorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
