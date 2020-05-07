from django.db.models import Q
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

def students_list(request):
    filters = Q()

    if request.GET.get("fname"):
        filters |= Q(first_name=request.GET.get("fname"))
    if request.GET.get("lname"):
        filters |= Q(last_name=request.GET.get("lname"))
    if request.GET.get("email"):
        filters |= Q(last_name=request.GET.get("email"))
    qs = Student.objects.filter(filters)
    result = "<br>".join(
        str(student)
        for student in qs
    )
    return render(
        request=request,
        template_name="student_list.html",
        context={'students_list': result}
    )
