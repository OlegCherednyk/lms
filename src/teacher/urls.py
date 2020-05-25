from django.urls import path

from teacher.views import TeacherCreateViews, TeacherListView, \
    TeacherUpdateViews, TeacherDeleteViews

app_name = 'teacher'

urlpatterns = [
    path('', TeacherListView.as_view(), name='list'),
    path('edit/<int:pk>', TeacherUpdateViews.as_view(), name='edit'),
    path('del/<int:pk>', TeacherDeleteViews.as_view(), name='del'),
    path('add', TeacherCreateViews.as_view(), name='add'),
]
