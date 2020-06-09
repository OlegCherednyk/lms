# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, CreateView, ListView

from group.forms import GroupAddForm, GroupEditForm
from group.models import Group


class GroupListView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'group_list.html'
    context_object_name = 'group_list'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        request = self.request
        qs = super().get_queryset()
        qs = qs.order_by('-id')

        if request.GET.get('group_name'):
            qs = qs.filter(group_num=request.GET.get('group_name'))

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = "Group list"
        return context


class GroupUpdateViews(LoginRequiredMixin, UpdateView):
    model = Group
    template_name = 'group_edit.html'
    form_class = GroupEditForm
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('group:list')


class GroupCreateViews(LoginRequiredMixin, CreateView):
    model = Group
    template_name = 'group_add.html'
    form_class = GroupAddForm
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('group:list')
