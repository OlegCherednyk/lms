from django.shortcuts import render
from student.models import Student
from django.http import HttpResponse
# Create your views here.
def gen_student(request):
    c = 0
    for i in range(int(request.GET.get("count",0))):
        c += 1
        Student.gen_student()
    return HttpResponse(f"you create {c} students")
