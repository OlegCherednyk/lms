from django.shortcuts import render

# Create your views here.
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
