from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from group.forms import GroupAddForm
from group.models import Group


def group_list(request):
    qs = Group.objects.all()
    if request.GET.get("group_name"):
        qs = qs.filter(last_name=request.GET.get("group_name"))
    result = "<br>".join(
        str(group)
        for group in qs
    )
    return render(
        request=request,
        template_name="group_list.html",
        context={'group_list': result}
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
        context={'form': form}
    )
