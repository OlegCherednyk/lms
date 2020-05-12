from django.forms import ModelForm

from teacher.models import Teacher


class TeacherAddForm(ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"


class TeacherEditForm(ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"
