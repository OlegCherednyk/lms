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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from group.views import group_list, groups_add, groups_edit
from student.views import gen_student, students_list, students_add, students_edit, del_students
from teacher.views import teacher_list, teachers_add, teachers_edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', gen_student),
    path('students/', students_list, name='student'),
    path('students/add', students_add),
    path('students/del', del_students),
    path('students/edit/<int:id>', students_edit),

    path('teacher/', teacher_list, name='teacher'),
    path('teacher/edit/<int:id>', teachers_edit),
    path('teacher/add', teachers_add),

    path('group/', group_list, name='group'),
    path('group/add', groups_add),
    path('group/edit/<int:id>', groups_edit),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
