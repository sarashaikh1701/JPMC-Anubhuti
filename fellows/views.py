from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import StudentSerializer,FellowSerializer
from .models import Student,Fellows_table

# Create your views here.
'''
@api_view(['GET'])
def index(request):
    api_urls = {
        'List': '/fellows-list/',
        'Detail View': '/fellows-detail/<int:pk>/',
        'Create': '/fellows-create/',
        'Update': '/fellows-update/<int:id>/',
        'Delete': '/fellows-delete/<int:id>/',
    }
    
    return Response(api_urls)
    #return HttpResponse('Hello from fellows')
    #return render(request, 'fellows/index.html')'''

@api_view(['GET'])
def ShowAll(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewStudent(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreateStudent(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['POST'])
def UpdateStudent(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['GET', 'DELETE'])
def DeleteStudent(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return Response('Item deleted')

@api_view(['GET'])
def fellowlist(request):
    fellows = Fellows_table.objects.all()
    serializer = FellowSerializer(fellows,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def fellowDetail(request, pk):
    fellows = Fellows_table.objects.get(id=pk)
    serializer = FellowSerializer(fellows,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def fellowCreate(request):
    serializer = FellowSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def fellowUpdate(request, pk):
    fellows = Fellows_table.objects.get(id=pk)
    serializer = FellowSerializer(instance = fellows, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def fellowDelete(request, pk):
    fellows = Fellows_table.objects.get(id=pk)
    fellows.delete()
    fellow = Fellows_table.objects.all()
    serializer = FellowSerializer(fellow,many=True)
    return Response(serializer.data)
