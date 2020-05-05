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
    qs0 = Student.objects.all()

    if request.GET.get("lname"):
        qs1 = qs0.filter(last_name=request.GET.get("lname"))
    else:
        qs1 = qs0.none()
    if request.GET.get("fname"):
        qs2 = qs0.filter(first_name=request.GET.get("fname"))
    else:
        qs2 = qs0.none()
    if request.GET.get("email"):
        qs3 = qs0.filter(email=request.GET.get("email"))
    else:
        qs3 = qs0.none()
    qs = qs1.union(qs2, qs3, qs1)
    result = "<br>".join(
        str(student)
        for student in qs
    )
    return render(
        request=request,
        template_name="student_list.html",
        context={'students_list': result}
    )
