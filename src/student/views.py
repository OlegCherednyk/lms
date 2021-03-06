from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from student.forms import StudentAddForm, StudentEditForm
from student.models import Student


# Create your views here.
def gen_student(request):
    c = 0
    for i in range(int(request.GET.get("count", 0))):
        c += 1
        Student.gen_student()
    return HttpResponse(f"you create {c} students")


class StudentsListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students_list'
    login_url = reverse_lazy('login')
    paginate_by = 50

    def get_queryset(self):
        request = self.request
        qs = super().get_queryset()
        qs = qs.select_related('group')
        qs = qs.order_by('-id')

        if request.GET.get('fname'):
            qs = qs.filter(first_name=request.GET.get('fname'))

        if request.GET.get('lname'):
            qs = qs.filter(last_name=request.GET.get('lname'))

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = "Student list"
        return context


class StudentsUpdateViews(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = 'students_edit.html'
    form_class = StudentEditForm
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('students:list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = "Edit student"
        return context


class StudentsCreateViews(LoginRequiredMixin, CreateView):
    model = Student
    template_name = 'students_add.html'
    form_class = StudentAddForm
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('students:list')


class StudentsDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'students_del.html'

    def get_success_url(self):
        return reverse('students:list')
