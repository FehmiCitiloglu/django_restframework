from django.urls import path
from api.views import EmployeeList, EmployeeDetail

urlpatterns = [
    path('employees/', EmployeeList.as_view()),
    path('employees/{id}', EmployeeDetail.as_view()),
    
    ]