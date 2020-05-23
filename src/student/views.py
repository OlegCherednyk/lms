from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from student.forms import StudentAddForm, StudentEditForm, StudentDelForm
from student.models import Student
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound


# Create your views here.
def gen_student(request):
    c = 0
    for i in range(int(request.GET.get("count", 0))):
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
    qs = Student.objects.filter(filters).select_related("group")
    return render(
        request=request,
        template_name="student_list.html",
        context={'students_list': qs,
                 'title': 'Student list'
                 }
    )


def students_add(request):
    qs = Student.objects.all()
    qs = qs.filter(first_name=request.POST.get("first_name")
                   ).filter(last_name=request.POST.get("last_name")
                            ).filter(email=request.POST.get("email")
                                     ).filter(phone_number=request.POST.get("phone_number"))

    check = qs.count()
    if request.method == 'POST':
        form = StudentAddForm(request.POST)

        if not check:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('student'))
        else:
            return HttpResponse('Этот студент уже существует, попробуйте ещё раз ', status=409)
    else:
        form = StudentAddForm()

    return render(
        request=request,
        template_name="students_add.html",
        context={'form': form,
                 'title': 'Add student'
                 }
    )


def students_edit(request, id):
    try:
        student = Student.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("Student with this id not exist ")
    if request.method == 'POST':
        form = StudentEditForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('student'))
        else:
            return HttpResponse('Этот студент уже существует, попробуйте ещё раз ', status=409)
    else:
        form = StudentEditForm(
            instance=student
        )
    return render(
        request=request,
        template_name="students_edit.html",
        context={'form': form,
                 'title': 'Edit student'
                 }
    )


def del_students(request):
    filters = Q()

    if request.GET.get("fname"):
        filters |= Q(first_name=request.GET.get("fname"))
    if request.GET.get("lname"):
        filters |= Q(last_name=request.GET.get("lname"))
    if request.GET.get("email"):
        filters |= Q(last_name=request.GET.get("email"))
    qs = Student.objects.filter(filters)
    if request.method == "POST":
        qs.delete()
        return HttpResponseRedirect(reverse('student'))
    return render(
        request=request,
        template_name="students_del.html",
        context={
            'del_list': qs,
            'title': 'Delete some students'
        }
    )
