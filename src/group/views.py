from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from group.forms import GroupAddForm, GroupEditForm
from group.models import Group


def group_list(request):
    qs = Group.objects.all()
    if request.GET.get("group_name"):
        qs = qs.filter(group_num=request.GET.get("group_name"))
    return render(
        request=request,
        template_name="group_list.html",
        context={'group_list': qs,
                 'title': "Group list"
                 }
    )


def groups_add(request):

    if request.method == 'POST':
        form = GroupAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('group'))
    else:
        form = GroupAddForm()

    return render(
        request=request,
        template_name="group_add.html",
        context={'form': form,
                 'title': 'Add group'
                 }
    )


def groups_edit(request, id):
    try:
        group = Group.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("Teacher with this id not exist ")
    if request.method == 'POST':
        form = GroupEditForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('group'))
        else:
            return HttpResponse('Эта группа уже существует, попробуйте ещё раз ', status=409)
    else:
        form = GroupEditForm(
            instance=group
        )
    return render(
        request=request,
        template_name="group_edit.html",
        context={'form': form,
                 'title': 'Edit group'
                 }
    )
