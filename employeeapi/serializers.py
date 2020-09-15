from rest_framework import serializers
from .models import Employee,Notes,User

 
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model =Employee
        fields = '__all__'


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model =Notes
        fields= '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'