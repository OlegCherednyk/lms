from django.contrib import admin

# Register your models here.
from group.models import Group
from student.models import Student
from teacher.models import Teacher


class StudentAdminModel(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'email', 'group', 'phone_number')
    list_display = ('first_name', 'last_name', 'email', 'group')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.select_related('group')
        return qs



admin.site.register(Student, StudentAdminModel)

