from django.db.models import fields
from rest_framework import serializers
from api.models import Employee


class Serializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'
        
class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=225)
    email = serializers.EmailField()
    age = serializers.IntegerField()
    salary = serializers.DecimalField(max_digits=11, decimal_places=2)
    location = serializers.CharField(max_length=125)