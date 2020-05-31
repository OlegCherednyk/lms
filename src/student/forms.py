from django.core.exceptions import ValidationError
from django.forms import ModelForm

from student.models import Student


class StudentAddForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class StudentEditForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

    def clean_email(self):
        id = self.instance.id
        email = self.cleaned_data['email']
        if Student.objects.all().filter(email=email).exclude(id=id).exists():
            raise ValidationError('Email already exists')
        return email

    def clean(self):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        id = self.instance.id
        if Student.objects.all().filter(first_name=first_name, last_name=last_name).exclude(id=id).exists():
            raise ValidationError('This person already exists')
        return self.cleaned_data

class StudentDelForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
