from django.shortcuts import render
from rest_framework.views import  APIView
from restapi.models import Employee
from restapi.serilizers import EmployeeSerilizer
from django.http import HttpResponse
from rest_framework.response import Response
import json
from restapi.PasswordHasher import PasswordHasher

class Employeelist(APIView):

    def get(self,request):
        employee = Employee.objects.all()
        serilizer = EmployeeSerilizer(employee,many=True)
        return Response(serilizer.data)

class EmployeeSave(APIView):
    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            self.validate_and_save_employee_details(body=body)
        except Exception as e:
            return Response({"result": "User could not be created"},status=419)
        return Response({"result": "OK"},status=200)

    def validate_and_save_employee_details(self,body):
        if body.get("password") == body.get("cnf_password") and body.get("first_name") is not None and body.get("first_name") is not "":
            body.pop('cnf_password')
            passwordHasher = PasswordHasher()
            body['password'] = passwordHasher.hash_password(body.get("password"))
            emp = Employee(**body)
            emp.save()
        else:
            raise Exception()


 # class Signin(APIView):
 #      def get(self,request):
 #


