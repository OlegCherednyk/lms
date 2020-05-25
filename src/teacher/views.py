# Create your views here.
from django.urls import reverse
from django.views.generic import UpdateView, CreateView, DeleteView, ListView

from teacher.forms import TeacherAddForm, TeacherEditForm
from teacher.models import Teacher


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teacher_list.html'
    context_object_name = 'teacher_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = "Teacher list"
        return context


class TeacherUpdateViews(UpdateView):
    model = Teacher
    template_name = 'teacher_edit.html'
    form_class = TeacherEditForm

    def get_success_url(self):
        return reverse('teacher:list')


class TeacherCreateViews(CreateView):
    model = Teacher
    template_name = 'teacher_add.html'
    form_class = TeacherAddForm

    def get_success_url(self):
        return reverse('teacher:list')


class TeacherDeleteViews(DeleteView):
    model = Teacher
    template_name = 'teacher_del.html'

    def get_success_url(self):
        return reverse('teacher:list')
