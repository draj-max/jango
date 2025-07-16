from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404

from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.


class EmployeeListCreateAPIView(APIView):
    """
    API view to list and create Employee instances.
    """
    permission_classes = [AllowAny]

    print("\nEmployeeListCreateAPIView initialized\n")

    def get(self, request):
        """
        Handle GET requests to list all employees.
        """
        employees = Employee.objects.all()
        print("Fetching all employees")
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Handle POST requests to create a new employee.
        """
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeUpdatedDeleteAPIView(APIView):
    """
    API view to retrieve, update, or delete a specific Employee instance.
    """
    permission_classes = [AllowAny]

    def get_object(self, pk):
        """
        Helper method to get an Employee instance by primary key.
        """
        return get_object_or_404(Employee, pk=pk)

    def get(self, request, pk):
        """
        Handle GET requests to retrieve a specific employee by ID.
        """
        employee = self.get_object(pk)
        print(f"Fetching employee with ID: {pk}")
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        """
        Handle PUT requests to update a specific employee.
        """
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(
            employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """
        Handle PUT requests to update a specific employee.
        """
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(
            employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Soft or hard delete based on ?hard=true
        """
        employee = self.get_object(pk)
        hard = request.query_params.get('hard') == 'true'

        if hard:
            employee.delete()
            return Response({"detail": "Hard delete performed."}, status=status.HTTP_204_NO_CONTENT)
        else:
            employee.is_active = False
            employee.save()
            return Response({"detail": "Soft delete performed."}, status=status.HTTP_204_NO_CONTENT)
