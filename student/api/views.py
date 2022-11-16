from api.models import Student
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import StudentSerializer

@api_view(['GET'])
def index(request):
    students = Student.objects.all()
    serialstudents = StudentSerializer(students, many=True)
    return JsonResponse(serialstudents.data, safe=False)

@api_view(["GET"])
def studentView(request, pk):
    student = Student.objects.get(id=pk)
    serialstudent = StudentSerializer(student,many=False)
    return JsonResponse(serialstudent.data)


@api_view(["POST"])
def studentAdd( request):
    serialdata = StudentSerializer(data=request.data)
    if serialdata.is_valid():
        serialdata.save()
    
    return JsonResponse(serialdata.data)

@api_view(["POST"])
def studentUpdate( request, pk):
    student = Student.objects.get(id = pk)
    serialstudent = StudentSerializer(instance=student, data=request.data)
     
    if serialstudent.is_valid():
        serialstudent.save()
    
    return JsonResponse(serialstudent.data)

@api_view(["DELETE"])
def studentdelete( request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    
    students= Student.objects.all()
    serialstudents = StudentSerializer(students, many=True)

    return JsonResponse(serialstudents.data, safe=False)
    
       
