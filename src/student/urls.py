from django.urls import path

from student.views import StudentsListView, \
    StudentsUpdateViews, StudentsCreateViews, StudentsDeleteView

app_name = 'students'

urlpatterns = [
    path('', StudentsListView.as_view(), name='list'),
    path('add/', StudentsCreateViews.as_view(), name='add'),
    path('del/<int:pk>', StudentsDeleteView.as_view(), name='del'),
    path('edit/<int:pk>', StudentsUpdateViews.as_view(), name='edit'),
]
