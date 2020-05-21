from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from teacher.forms import TeacherAddForm, TeacherEditForm
from teacher.models import Teacher


def teacher_list(request):
    qs = Teacher.objects.all()
    if request.GET.get("lname"):
        qs = qs.filter(last_name=request.GET.get("lname"))
    if request.GET.get("fname"):
        qs = qs.filter(first_name=request.GET.get("fname"))
    if request.GET.get("email"):
        qs = qs.filter(email=request.GET.get("email"))

    return render(
        request=request,
        template_name="teacher_list.html",
        context={'teacher_list': qs,
                 'title': 'Teachers list'
                 }
    )


def teachers_add(request):

    if request.method == 'POST':
        form = TeacherAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teacher'))
    else:
        form = TeacherAddForm()

    return render(
        request=request,
        template_name="teachers_add.html",
        context={'form': form,
                 'title': 'Add teacher'
                 }
    )


def teachers_edit(request, id):
    try:
        teacher = Teacher.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("Teacher with this id not exist ")
    if request.method == 'POST':
        form = TeacherEditForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teacher'))
        else:
            return HttpResponse('Этот учитель   уже существует, попробуйте ещё раз ', status=409)
    else:
        form = TeacherEditForm(
            instance=teacher
        )
    return render(
        request=request,
        template_name="teacher_edit.html",
        context={'form': form,
                 'title': 'Edit teacher'
                 }
    )
