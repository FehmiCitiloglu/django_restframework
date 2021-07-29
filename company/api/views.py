from django.db.models.query import QuerySet
from django.shortcuts import render

from rest_framework import generics
from api.models import Employee
from api.serializers import EmployeeSerializer, Serializer


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    querySet = Employee.objects.all()
    serializer_class = EmployeeSerializer