"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from group.views import group_list,groups_add
from student.views import gen_student, students_list,students_add
from teacher.views import teacher_list,teachers_add

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', gen_student),
    path('students/', students_list, name='student'),
    path('students/add', students_add),

    path('teacher/', teacher_list, name='teacher'),
    path('teacher/add', teachers_add),
    path('group/', group_list, name='group'),
    path('group/add', groups_add),


]
