from django.shortcuts import render

# Create your views here.
from teacher.models import Teacher


def teacher_list(request):
    qs = Teacher.objects.all()
    if request.GET.get("lname"):
        qs = qs.filter(last_name=request.GET.get("lname"))
    if request.GET.get("fname"):
        qs = qs.filter(first_name=request.GET.get("fname"))
    if request.GET.get("email"):
        qs = qs.filter(email=request.GET.get("email"))

    result = "<br>".join(
        str(teacher)
        for teacher in qs
    )
    return render(
        request=request,
        template_name="teacher_list.html",
        context={'teacher_list': result}
    )
