from django.http import HttpResponse
from django.urls import reverse
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


class StudentsListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students_list'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related("group")
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = "Student list"
        return context


class StudentsUpdateViews(UpdateView):
    model = Student
    template_name = 'students_edit.html'
    form_class = StudentEditForm

    def get_success_url(self):
        return reverse('students:list')


class StudentsCreateViews(CreateView):
    model = Student
    template_name = 'students_add.html'
    form_class = StudentAddForm

    def get_success_url(self):
        return reverse('students:list')


class StudentsDeleteView(DeleteView):
    model = Student
    template_name = 'students_del.html'

    def get_success_url(self):
        return reverse('students:list')
